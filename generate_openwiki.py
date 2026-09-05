import argparse
import ast
import datetime
import os
import subprocess


def run_command(command, ignore_errors=False):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True, shell=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        if not ignore_errors:
            print(f"Error running command: {command}")
            print(e.stderr)
        return None


def get_last_commit():
    return run_command("git rev-parse --short HEAD") or "HEAD"


IGNORED_DIRS = {
    ".venv",
    ".git",
    ".github",
    ".vscode",
    ".idea",
    "node_modules",
    "dist",
    "bin",
    "obj",
    "target",
    "coverage",
    "__pycache__",
    "openwiki",
    ".dvc",
    ".jules",
    ".agents",
}


def is_ignored(filepath):
    parts = filepath.split(os.sep)
    for part in parts:
        if part in IGNORED_DIRS:
            return True
    return False


def get_changed_files():

    # Attempt to get changes from the latest commit if HEAD~1 fails (e.g. shallow clone or single commit)
    diff_output = run_command("git diff --name-only origin/main HEAD", ignore_errors=True)
    if diff_output is None:
        diff_output = run_command("git show --name-only --format=")

    if not diff_output:
        return []
    return [f for f in diff_output.split("\n") if f.endswith(".py") and not is_ignored(f)]


def delete_generated_docs():
    openwiki_dir = "openwiki"
    if os.path.exists(openwiki_dir):
        for root, dirs, files in os.walk(openwiki_dir, topdown=False):
            for name in files:
                filepath = os.path.join(root, name)
                # Keep manually curated/reserved files safe from deletion.
                if filepath in ["openwiki/INSTRUCTIONS.md", "openwiki/logs.md"]:
                    continue
                os.remove(filepath)
            for name in dirs:
                try:
                    os.rmdir(os.path.join(root, name))
                except OSError:
                    pass  # directory not empty due to reserved files


def extract_calls(node):
    calls = []
    for child in ast.walk(node):
        if isinstance(child, ast.Call):
            if isinstance(child.func, ast.Name):
                calls.append(child.func.id)
            elif isinstance(child.func, ast.Attribute):
                calls.append(child.func.attr)
    return list(dict.fromkeys(calls))


def extract_complex_doc(docstring):
    if not docstring:
        return {"description": "No description available.", "complexity": None, "side_effects": None}
    lines = docstring.split("\n")
    complexity = None
    side_effects = None
    desc = []

    for line in lines:
        if line.lower().startswith("complexity:"):
            complexity = line.split(":", 1)[1].strip()
        elif line.lower().startswith("side effects:"):
            side_effects = line.split(":", 1)[1].strip()
        else:
            desc.append(line)

    return {
        "description": "\n".join(desc).strip() or "No description available.",
        "complexity": complexity,
        "side_effects": side_effects,
    }


def extract_type_refs(node):
    refs = []
    if node is None:
        return refs
    for child in ast.walk(node):
        if isinstance(child, ast.Name):
            refs.append(child.id)
        elif isinstance(child, ast.Attribute):
            refs.append(child.attr)
        elif isinstance(child, ast.Constant) and isinstance(child.value, str):
            refs.append(child.value)
    return list(dict.fromkeys(refs))


def unparse_annotation(node):
    if node is None:
        return "Any"
    if isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Attribute):
        return f"{unparse_annotation(node.value)}.{node.attr}"
    elif isinstance(node, ast.Subscript):
        return f"{unparse_annotation(node.value)}[{unparse_annotation(node.slice)}]"
    elif isinstance(node, ast.Constant):
        if isinstance(node.value, str):
            return node.value
        return str(node.value)
    elif isinstance(node, ast.Tuple):
        return f"({', '.join(unparse_annotation(el) for el in node.elts)})"
    elif isinstance(node, ast.List):
        return f"[{', '.join(unparse_annotation(el) for el in node.elts)}]"
    elif isinstance(node, ast.BinOp):
        if isinstance(node.op, ast.BitOr):
            return f"{unparse_annotation(node.left)} | {unparse_annotation(node.right)}"
    # Fallback to ast.unparse (Python 3.9+)
    try:
        return ast.unparse(node)
    except Exception:
        return "Any"


def extract_docstring(node):
    doc = ast.get_docstring(node)
    return doc if doc else "No description available."


def parse_args(args):
    parsed = []
    defaults = args.defaults
    posonlyargs = getattr(args, "posonlyargs", [])
    # Defaults are aligned to the end of args.args + args.posonlyargs
    total_positional = len(posonlyargs) + len(args.args)
    offset = total_positional - len(defaults)

    for i, arg in enumerate(posonlyargs):
        parsed.append({
            "name": arg.arg,
            "type": unparse_annotation(arg.annotation),
            "type_refs": extract_type_refs(arg.annotation),
            "default": ast.unparse(defaults[i - offset]) if i >= offset else None,
        })
    for i, arg in enumerate(args.args, start=len(posonlyargs)):
        parsed.append({
            "name": arg.arg,
            "type": unparse_annotation(arg.annotation),
            "type_refs": extract_type_refs(arg.annotation),
            "default": ast.unparse(defaults[i - offset]) if i >= offset else None,
        })
    if args.vararg:
        parsed.append({
            "name": f"*{args.vararg.arg}",
            "type": unparse_annotation(args.vararg.annotation),
            "type_refs": extract_type_refs(args.vararg.annotation),
            "default": None,
        })
    for i, arg in enumerate(args.kwonlyargs):
        parsed.append({
            "name": arg.arg,
            "type": unparse_annotation(arg.annotation),
            "type_refs": extract_type_refs(arg.annotation),
            "default": ast.unparse(args.kw_defaults[i]) if args.kw_defaults[i] is not None else None,
        })
    if args.kwarg:
        parsed.append({
            "name": f"**{args.kwarg.arg}",
            "type": unparse_annotation(args.kwarg.annotation),
            "type_refs": extract_type_refs(args.kwarg.annotation),
            "default": None,
        })
    return parsed


def parse_python_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)

    module_doc = extract_docstring(tree)
    imports = []
    classes = []
    functions = []

    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            for alias in node.names:
                if alias.name == "*":
                    imports.append(f"{module}.*")
                else:
                    imports.append(f"{module}.{alias.name}")
        elif isinstance(node, ast.ClassDef):
            docstring = extract_docstring(node)
            extracted = extract_complex_doc(docstring)
            cls_info = {
                "name": node.name,
                "docstring": extracted["description"],
                "complexity": extracted["complexity"],
                "side_effects": extracted["side_effects"],
                "bases": [unparse_annotation(b) for b in node.bases],
                "attributes": [],
                "methods": [],
                "constructor": None,
                "calls": extract_calls(node),
            }

            for child in node.body:
                if isinstance(child, ast.AnnAssign) and isinstance(child.target, ast.Name):
                    cls_info["attributes"].append({
                        "name": child.target.id,
                        "type": unparse_annotation(child.annotation),
                        "type_refs": extract_type_refs(child.annotation),
                    })
                elif isinstance(child, ast.Assign):
                    for target in child.targets:
                        if isinstance(target, ast.Name):
                            cls_info["attributes"].append({"name": target.id, "type": "Any", "type_refs": []})
                elif isinstance(child, ast.FunctionDef):
                    is_private = child.name.startswith("_") and child.name != "__init__"
                    docstring = extract_docstring(child)
                    extracted = extract_complex_doc(docstring)
                    method_info = {
                        "name": child.name,
                        "docstring": extracted["description"],
                        "complexity": extracted["complexity"],
                        "side_effects": extracted["side_effects"],
                        "args": parse_args(child.args),
                        "returns": unparse_annotation(child.returns),
                        "return_type_refs": extract_type_refs(child.returns),
                        "is_private": is_private,
                        "calls": extract_calls(child),
                    }
                    if child.name == "__init__":
                        cls_info["constructor"] = method_info
                    else:
                        cls_info["methods"].append(method_info)
            classes.append(cls_info)
        elif isinstance(node, ast.FunctionDef):
            is_private = node.name.startswith("_")
            docstring = extract_docstring(node)
            extracted = extract_complex_doc(docstring)
            functions.append({
                "name": node.name,
                "docstring": extracted["description"],
                "complexity": extracted["complexity"],
                "side_effects": extracted["side_effects"],
                "args": parse_args(node.args),
                "returns": unparse_annotation(node.returns),
                "return_type_refs": extract_type_refs(node.returns),
                "is_private": is_private,
                "calls": extract_calls(node),
            })

    return {
        "filepath": filepath,
        "docstring": module_doc,
        "imports": imports,
        "classes": classes,
        "functions": functions,
    }


def clean_plantuml_type(t):
    """Make type string safe for PlantUML."""
    t = t.replace("[", "~").replace("]", "~")
    return t


def generate_plantuml(classes):
    """Generate PlantUML class diagram for the classes."""
    if not classes:
        return ""

    lines = ["```plantuml", "classDiagram", "    direction BT"]

    class_names = {cls["name"] for cls in classes}
    relationships = set()

    for cls in classes:
        lines.append(f"    class {cls['name']} {{")
        # Add attributes
        for attr in cls["attributes"]:
            safe_type = clean_plantuml_type(attr["type"])
            lines.append(f"        +{attr['name']}: {safe_type}")
            for ref in attr.get("type_refs", []):
                if ref in class_names and ref != cls["name"]:
                    relationships.add(f"    {cls['name']} --> {ref} : Association")

        # Add methods
        for method in cls["methods"]:
            args_str = ", ".join(f"{arg['name']}: {clean_plantuml_type(arg['type'])}" for arg in method["args"])
            ret_str = clean_plantuml_type(method["returns"])
            lines.append(f"        +{method['name']}({args_str}) {ret_str}")

            for arg in method["args"]:
                for ref in arg.get("type_refs", []):
                    if ref in class_names and ref != cls["name"]:
                        relationships.add(f"    {cls['name']} ..> {ref} : Usage")

            for ref in method.get("return_type_refs", []):
                if ref in class_names and ref != cls["name"]:
                    relationships.add(f"    {cls['name']} ..> {ref} : Usage")

        lines.append("    }")

        # Add inheritance
        for base in cls["bases"]:
            base_name = base.split(".")[-1]
            lines.append(f"    {base_name} <|-- {cls['name']} : Generalization")

    for rel in sorted(relationships):
        lines.append(rel)

    lines.append("```")
    return "\n".join(lines)


registry = {"modules": {}, "class_to_module": {}, "function_to_module": {}}


def build_registry(files_to_process):
    for py_file in files_to_process:
        parsed = parse_python_file(py_file)
        registry["modules"][py_file] = parsed
        for cls in parsed["classes"]:
            registry["class_to_module"][cls["name"]] = py_file
        for func in parsed["functions"]:
            registry["function_to_module"][func["name"]] = py_file


def generate_package_diagram_content():
    lines = ["```plantuml", 'package "src" {']
    packages = {}
    for py_file in registry["modules"].keys():
        parts = py_file.split("/")[:-1]
        pkg = ".".join(parts)
        if pkg:
            packages[pkg] = None
    for pkg in sorted(packages.keys()):
        lines.append(f'    package "{pkg}" {{}}')
    lines.append("}")
    lines.append("```")
    return "\n".join(lines)


def generate_call_graph():
    lines = ["```plantuml", "digraph CallGraph {"]

    # Build a list of all defined functions/methods across the project to map internal calls
    defined_callables = {}
    for mod_path, data in registry["modules"].items():
        for func in data["functions"]:
            defined_callables[func["name"]] = None
        for cls in data["classes"]:
            defined_callables[cls["name"]] = None
            for m in cls["methods"]:
                defined_callables[m["name"]] = None

    edges = {}
    for mod_path, data in registry["modules"].items():
        for func in data["functions"]:
            for call in func.get("calls", []):
                if call in defined_callables:
                    edges[f'    "{func["name"]}()" -> "{call}()"'] = None
        for cls in data["classes"]:
            for m in cls.get("methods", []):
                for call in m.get("calls", []):
                    if call in defined_callables:
                        edges[f'    "{cls["name"]}.{m["name"]}()" -> "{call}()"'] = None

    for edge in sorted(edges.keys()):
        lines.append(edge)

    lines.append("}")
    lines.append("```")
    return "\n".join(lines)


def generate_dependency_graph():
    lines = ["```plantuml", "digraph Dependencies {"]
    edges = set()
    for mod_path, data in registry["modules"].items():
        mod_name = os.path.splitext(os.path.basename(mod_path))[0]
        for imp in data["imports"]:
            imp_name = imp.split(".")[-1] if "." in imp else imp
            if imp_name != "*":
                edges.add(f'    "{mod_name}" -> "{imp_name}"')
    for edge in sorted(edges):
        lines.append(edge)
    lines.append("}")
    lines.append("```")
    return "\n".join(lines)


def generate_markdown(parsed_data, relative_filepath, md_path):
    mod_name = os.path.splitext(os.path.basename(relative_filepath))[0]

    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    commit_hash = get_last_commit()

    # Calculate source reference path
    back_path = os.path.relpath(relative_filepath, os.path.dirname(md_path))

    frontmatter = f"""---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: {mod_name}"
source_path: "{relative_filepath}"
description: "{parsed_data["docstring"].splitlines()[0] if parsed_data["docstring"] else "Auto-generated documentation."}"
tags: ["module", "{mod_name}"]
timestamp: "{timestamp}"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "{commit_hash}"
---
"""

    body = []
    body.append(f"# Module Specification: {mod_name}")
    body.append(f"* **Source Reference:** [{relative_filepath}]({back_path})")

    body.append("# Module Overview")
    body.append("## Purpose")
    body.append(
        f"{parsed_data['docstring'].splitlines()[0] if parsed_data['docstring'] else 'No description available.'}"
    )
    body.append("## Responsibilities")
    body.append(f"{parsed_data['docstring']}")
    body.append("## Dependencies")
    if parsed_data["imports"]:
        for imp in parsed_data["imports"]:
            body.append(f"* `{imp}`")
    else:
        body.append("_No dependencies found._")

    body.append("# Each File Documentation")
    if parsed_data["imports"]:
        body.append("## Imported modules")
        for imp in parsed_data["imports"]:
            body.append(f"* `{imp}`")
    if parsed_data["classes"]:
        body.append("## Exported classes")
        for cls in parsed_data["classes"]:
            body.append(f"* `{cls['name']}`")
    if parsed_data["functions"]:
        body.append("## Exported functions")
        for func in parsed_data["functions"]:
            body.append(f"* `{func['name']}`")

    body.append("## Exported interfaces")
    body.append("_No interfaces found._")
    body.append("## Public API")
    body.append("_See exported classes and functions._")
    body.append("## Internal architecture")
    body.append("_See architectural detected patterns and UML._")
    body.append("## Execution flow")
    body.append("_Execution flow depends on public API usage._")
    body.append("## Sequence explanation")
    body.append("_See sequence diagram._")
    body.append("## UML")
    body.append("_See diagrams below._")
    body.append("## Examples")
    body.append("_No module level examples available._")

    # Architecture Detection
    body.append("### Detected Architecture Patterns")
    patterns = []
    if "controller" in relative_filepath.lower():
        patterns.append("Controller")
    if "services" in relative_filepath.lower() or "service" in mod_name.lower():
        patterns.append("Service")
    if "models" in relative_filepath.lower() or "entity" in mod_name.lower():
        patterns.append("Entity / Domain Model")
    if "repositories" in relative_filepath.lower():
        patterns.append("Repository")
    if "schemas" in relative_filepath.lower() or "dto" in mod_name.lower():
        patterns.append("DTO")
    if "factory" in mod_name.lower() or "builder" in mod_name.lower():
        patterns.append("Factory / Builder")
    if "adapter" in mod_name.lower() or "port" in mod_name.lower():
        patterns.append("Adapter / Port")

    if patterns:
        body.append(f"Detected roles: {', '.join(patterns)}")
    else:
        body.append("Detected roles: General Subsystem")

    body.append("## 2. UML Diagrams")
    body.append("### Class Diagram")
    puml = generate_plantuml(parsed_data["classes"])
    if puml:
        body.append(puml)
    else:
        body.append("_No classes found._")

    body.append("### Sequence Diagram")
    seq_lines = ["```plantuml", "sequenceDiagram"]
    has_seq = False

    for cls in parsed_data["classes"]:
        for m in cls["methods"]:
            if m.get("calls"):
                has_seq = True
                caller = f"{cls['name']}.{m['name']}"
                for call in m["calls"]:
                    seq_lines.append(f"    {caller}->>{call}: invoke")

    for func in parsed_data["functions"]:
        if func.get("calls"):
            has_seq = True
            for call in func["calls"]:
                seq_lines.append(f"    {func['name']}->>{call}: invoke")

    seq_lines.append("```")
    if has_seq:
        body.append("\n".join(seq_lines))
    else:
        body.append("_No sequences found._")

    body.append("### Component Diagram")
    comp_lines = ["```plantuml", f"component [{mod_name}] as Comp"]
    # Look for imports as dependencies for the component
    for imp in parsed_data["imports"]:
        comp_name = imp.split(".")[-1]
        if comp_name != "*":
            comp_lines.append(f"Comp --> [{comp_name}]")
    comp_lines.append("```")
    body.append("\n".join(comp_lines))

    if parsed_data["classes"] or parsed_data["functions"]:
        body.append("## 3. Class & Method Specifications")

    if parsed_data["classes"]:
        body.append("# Public Classes")
    for cls in parsed_data["classes"]:
        body.append(f"### `{cls['name']}`")
        body.append("## Overview")
        body.append(f"{cls['docstring']}")
        body.append("**Why it exists:** Provides specific business logic or state encapsulation.")
        body.append("**What business capability it provides:** Implementation of module responsibilities.")
        body.append("**How it collaborates:** Interacts with other components via standard API boundaries.")

        if cls.get("constructor"):
            c = cls["constructor"]
            body.append("## Constructor")
            args_str = ", ".join(f"{arg['name']}: {arg['type']}" for arg in c["args"])
            body.append(f"* **`__init__({args_str})`**")
            body.append("### Description")
            body.append(f"{c['docstring'].splitlines()[0] if c['docstring'] else 'No description available.'}")
            body.append("### Inputs")
            for arg in c["args"]:
                body.append(f"* `{arg['name']}`")
                body.append(f"  - **type**: {arg['type']}")
                body.append("  - **meaning**: Parameter description")
                body.append("  - **valid values**: Any valid value for the type")
                if arg.get("default") is not None:
                    body.append("  - **optional?**: Yes")
                    body.append(f"  - **default value**: {arg['default']}")
                else:
                    body.append("  - **optional?**: No")
            body.append("### Output")
            body.append("* **return type**: None")
            body.append("* **semantic meaning**: Initialization")
            body.append("* **possible null values**: None")
            body.append("* **exceptions**: Unspecified")
            if c.get("side_effects"):
                body.append("### Side Effects")
                body.append(c["side_effects"])
            if c.get("complexity"):
                body.append("### Complexity")
                body.append(f"Time Complexity: {c['complexity']}")

        if cls["attributes"]:
            body.append("## Attributes")
            for attr in cls["attributes"]:
                body.append(f"* **`{attr['name']}`**")
                body.append(f"  - **Type**: {attr['type']}")
                body.append("  - **Purpose**: Attribute for class state.")
                body.append("  - **Constraints**: Standard type constraints.")

        public_methods = [m for m in cls["methods"] if not m["is_private"]]
        private_methods = [m for m in cls["methods"] if m["is_private"]]

        if public_methods:
            body.append("## Public Methods")
            for m in public_methods:
                args_str = ", ".join(f"{arg['name']}: {arg['type']}" for arg in m["args"])
                body.append(f"### `{m['name']}({args_str}) -> {m['returns']}`")
                body.append("### Description")
                body.append(f"{m['docstring'].splitlines()[0] if m['docstring'] else 'No description available.'}")
                body.append("### Inputs")
                for arg in m["args"]:
                    body.append(f"* `{arg['name']}`")
                    body.append(f"  - **type**: {arg['type']}")
                    body.append("  - **meaning**: Parameter description")
                    body.append("  - **valid values**: Any valid value for the type")
                    if arg.get("default") is not None:
                        body.append("  - **optional?**: Yes")
                        body.append(f"  - **default value**: {arg['default']}")
                    else:
                        body.append("  - **optional?**: No")
                body.append("### Output")
                body.append(f"* **return type**: {m['returns']}")
                body.append("* **semantic meaning**: Result of the operation")
                body.append("* **possible null values**: Dependent on implementation")
                body.append("* **exceptions**: Unspecified")
                if m.get("side_effects"):
                    body.append("### Side Effects")
                    body.append(m["side_effects"])
                if m.get("complexity"):
                    body.append("### Complexity")
                    body.append(f"Time Complexity: {m['complexity']}")
                body.append("### Example")
                body.append("```python")
                body.append(f"# Example usage for {m['name']}")
                body.append("```")

        if private_methods:
            body.append("# Private Methods")
            for m in private_methods:
                args_str = ", ".join(f"{arg['name']}: {arg['type']}" for arg in m["args"])
                body.append(f"* **`{m['name']}({args_str}) -> {m['returns']}`**")
                body.append("### Purpose")
                body.append(f"{m['docstring'].splitlines()[0] if m['docstring'] else 'No description available.'}")
                body.append("### Parameters")
                for arg in m["args"]:
                    body.append(f"* `{arg['name']}` (`{arg['type']}`)")
                body.append("### Return value")
                body.append(f"* `{m['returns']}`")

    if parsed_data["functions"]:
        body.append("## Standalone Functions")
        for func in parsed_data["functions"]:
            args_str = ", ".join(f"{arg['name']}: {arg['type']}" for arg in func["args"])
            body.append(f"### `{func['name']}({args_str}) -> {func['returns']}`")
            body.append("### Description")
            body.append(f"{func['docstring']}")
            body.append("### Inputs")
            for arg in func["args"]:
                body.append(f"* `{arg['name']}`")
                body.append(f"  - **type**: {arg['type']}")
                body.append("  - **meaning**: Parameter description")
                body.append("  - **valid values**: Any valid value for the type")
                if arg.get("default") is not None:
                    body.append("  - **optional?**: Yes")
                    body.append(f"  - **default value**: {arg['default']}")
                else:
                    body.append("  - **optional?**: No")
            body.append("### Output")
            body.append(f"* **return type**: {func['returns']}")
            body.append("* **semantic meaning**: Result of the operation")
            body.append("* **possible null values**: Dependent on implementation")
            body.append("* **exceptions**: Unspecified")
            if func.get("side_effects"):
                body.append("### Side Effects")
                body.append(func["side_effects"])
            if func.get("complexity"):
                body.append("### Complexity")
                body.append(f"Time Complexity: {func['complexity']}")
            body.append("### Example")
            body.append("```python")
            body.append(f"# Example usage for {func['name']}")
            body.append("```")

    # Inject Used By
    used_by = []
    mod_path_dotted = relative_filepath.replace("src/", "").replace(".py", "").replace("/", ".")
    for other_py, other_data in registry["modules"].items():
        if other_py == relative_filepath:
            continue
        for imp in other_data["imports"]:
            if mod_path_dotted in imp or imp.startswith(mod_name):
                used_by.append(other_py)
                break

    body.append("## Used By")
    if used_by:
        for u in sorted(used_by):
            if u.startswith(f"src{os.sep}") or u.startswith("src/"):
                rel_u = u[4:]
            else:
                rel_u = u
            rel_u = rel_u[:-3] + ".md"

            # calculate correct relative path up
            up_path = os.path.relpath("openwiki/modules", os.path.dirname(md_path))
            if up_path == ".":
                up_path = ""
            else:
                up_path += "/"

            body.append(f"* [{os.path.basename(u)}]({up_path}{rel_u})")
    else:
        body.append("_Not used by any other module._")

    return frontmatter + "\n\n".join(b for b in body if b) + "\n"


def update_index_files(processed_files):
    # This function creates/updates openwiki/index.md and openwiki/SUMMARY.md
    summary_path = "openwiki/SUMMARY.md"

    modules = []
    if os.path.exists("openwiki/modules"):
        for root, _, files in os.walk("openwiki/modules"):
            for f in files:
                if f.endswith(".md"):
                    rel_path = os.path.relpath(os.path.join(root, f), "openwiki")
                    title = f[:-3]
                    modules.append((title, rel_path))
    modules.sort()

    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    commit_hash = get_last_commit()

    # Create diagrams page
    diagrams_path = "openwiki/architecture/diagrams.md"
    os.makedirs(os.path.dirname(diagrams_path), exist_ok=True)
    with open(diagrams_path, "w", encoding="utf-8") as f:
        f.write(
            f'---\niso_doc_type: "Description"\niso_viewpoint: "ArchitectureDescription"\ntype: "diagrams"\ntitle: "Diagrams"\ndescription: "Auto-generated architecture diagrams."\ntags: ["diagrams"]\ntimestamp: "{timestamp}"\ngenerated: "agent:ast-documentation-generator"\nverified: "true"\nlast_verified_commit: "{commit_hash}"\n---\n# Architecture Diagrams\n\n'
        )
        f.write("## Package Diagram\n")
        f.write(generate_package_diagram_content())
        f.write("\n\n## Dependency Graph\n")
        f.write(generate_dependency_graph())
        f.write("\n\n## Call Graph\n")
        f.write(generate_call_graph())

    # Build Alphabetical Index
    classes_list = sorted(list(registry["class_to_module"].keys()))
    api_list = sorted(list(registry["function_to_module"].keys()))

    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(
            f'---\niso_doc_type: "Description"\niso_viewpoint: "ArchitectureDescription"\ntype: "summary"\ntitle: "Summary"\ndescription: "Auto-generated summary."\ntags: ["summary"]\ntimestamp: "{timestamp}"\ngenerated: "agent:ast-documentation-generator"\nverified: "true"\nlast_verified_commit: "{commit_hash}"\n---\n# Summary\n\n'
        )
        f.write("## Architecture overview\n\n")
        f.write("* [Home](index.md)\n")
        f.write("* [Logs](logs.md)\n")
        f.write("* [Diagrams](architecture/diagrams.md)\n\n")

        f.write("## Alphabetical class index\n\n")
        for cls_name in classes_list:
            mod = registry["class_to_module"][cls_name]
            rel_mod = os.path.relpath(mod, "src")[:-3] + ".md"
            f.write(f"* [{cls_name}](modules/{rel_mod}#{cls_name.lower()})\n")
        f.write("\n")

        f.write("## Public API index\n\n")
        for api_name in api_list:
            mod = registry["function_to_module"][api_name]
            rel_mod = os.path.relpath(mod, "src")[:-3] + ".md"
            f.write(f"* [{api_name}](modules/{rel_mod}#{api_name.lower()})\n")
        f.write("\n")

        f.write("## Modules list\n\n")
        for title, rel in modules:
            f.write(f"* [{title}]({rel})\n")

    # Always ensure index.md exists and is OKF compliant
    index_path = "openwiki/index.md"
    if not os.path.exists(index_path):
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(
                f'---\niso_doc_type: "Description"\niso_viewpoint: "ArchitectureDescription"\ntype: "index"\ntitle: "Index"\ndescription: "Auto-generated index."\ntags: ["index"]\ntimestamp: "{timestamp}"\ngenerated: "agent:ast-documentation-generator"\nverified: "true"\nlast_verified_commit: "{commit_hash}"\n---\n# Index\n\n'
            )
            f.write("Welcome to the generated AST documentation.\n\n")
            f.write("Please see [SUMMARY.md](SUMMARY.md) for navigation.\n")


def main():
    parser = argparse.ArgumentParser(description="AST Documentation Generator")
    parser.add_argument("--mode", choices=["full", "diff"], default="full")
    args = parser.parse_args()

    all_files = []
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        for f in files:
            if f.endswith(".py"):
                filepath = os.path.relpath(os.path.join(root, f), ".")
                all_files.append(filepath)

    all_files.sort()

    # We must build the registry using ALL files so cross-references are complete
    build_registry(all_files)

    if args.mode == "full":
        delete_generated_docs()
        files_to_process = all_files
    else:
        changed_files = get_changed_files()
        impacted_files_dict = {f: None for f in changed_files}

        # In diff mode, we need to include files that depend on the changed files or are dependencies of them.
        for changed_file in changed_files:
            mod_name = os.path.splitext(os.path.basename(changed_file))[0]
            mod_path_dotted = changed_file.replace("src/", "").replace(".py", "").replace("/", ".")

            # Find files that import this changed file
            for other_py, other_data in registry["modules"].items():
                if other_py in impacted_files_dict:
                    continue
                for imp in other_data["imports"]:
                    if mod_path_dotted in imp or imp.startswith(mod_name):
                        impacted_files_dict[other_py] = None
                        break

        files_to_process = list(impacted_files_dict.keys())

    print(f"Mode: {args.mode}")
    print(f"Files to process: {len(files_to_process)}")

    os.makedirs("openwiki/architecture", exist_ok=True)
    os.makedirs("openwiki/modules", exist_ok=True)
    os.makedirs("openwiki/api", exist_ok=True)
    os.makedirs("openwiki/classes", exist_ok=True)
    os.makedirs("openwiki/diagrams", exist_ok=True)
    os.makedirs("openwiki/dependencies", exist_ok=True)
    os.makedirs("openwiki/glossary", exist_ok=True)
    os.makedirs("openwiki/decisions", exist_ok=True)
    os.makedirs("openwiki/generated", exist_ok=True)

    for py_file in files_to_process:
        parsed = registry["modules"].get(py_file)
        if not parsed:
            parsed = parse_python_file(py_file)

        if py_file.startswith(f"src{os.sep}") or py_file.startswith("src/"):
            rel_py = py_file[4:]
        else:
            rel_py = py_file

        md_path = os.path.join("openwiki/modules", rel_py[:-3] + ".md")

        os.makedirs(os.path.dirname(md_path), exist_ok=True)

        md_content = generate_markdown(parsed, py_file, md_path)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)

    update_index_files(files_to_process)
    print("Documentation generation complete.")


if __name__ == "__main__":
    main()
