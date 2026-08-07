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


def get_changed_files():
    # Attempt to get changes from the latest commit if HEAD~1 fails (e.g. shallow clone or single commit)
    diff_output = run_command("git diff --name-only origin/main HEAD", ignore_errors=True)
    if diff_output is None:
        diff_output = run_command("git show --name-only --format=")

    if not diff_output:
        return []
    return [f for f in diff_output.split("\n") if f.endswith(".py") and f.startswith("src/")]


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
                    pass # directory not empty due to reserved files




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
    # Defaults are aligned to the end of args.args
    offset = len(args.args) - len(defaults)

    for i, arg in enumerate(args.args):
        parsed.append({
            "name": arg.arg,
            "type": unparse_annotation(arg.annotation),
            "default": ast.unparse(defaults[i - offset]) if i >= offset else None,
        })
    if args.vararg:
        parsed.append({
            "name": f"*{args.vararg.arg}",
            "type": unparse_annotation(args.vararg.annotation),
            "default": None,
        })
    if args.kwarg:
        parsed.append({
            "name": f"**{args.kwarg.arg}",
            "type": unparse_annotation(args.kwarg.annotation),
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
            cls_info = {
                "name": node.name,
                "docstring": extract_docstring(node),
                "bases": [unparse_annotation(b) for b in node.bases],
                "attributes": [],
                "methods": [],
            }

            for child in node.body:
                if isinstance(child, ast.AnnAssign) and isinstance(child.target, ast.Name):
                    cls_info["attributes"].append({
                        "name": child.target.id,
                        "type": unparse_annotation(child.annotation),
                    })
                elif isinstance(child, ast.Assign):
                    for target in child.targets:
                        if isinstance(target, ast.Name):
                            cls_info["attributes"].append({"name": target.id, "type": "Any"})
                elif isinstance(child, ast.FunctionDef):
                    is_private = child.name.startswith("_") and child.name != "__init__"
                    method_info = {
                        "name": child.name,
                        "docstring": extract_docstring(child),
                        "args": parse_args(child.args),
                        "returns": unparse_annotation(child.returns),
                        "is_private": is_private,
                    }
                    cls_info["methods"].append(method_info)
            classes.append(cls_info)
        elif isinstance(node, ast.FunctionDef):
            is_private = node.name.startswith("_")
            functions.append({
                "name": node.name,
                "docstring": extract_docstring(node),
                "args": parse_args(node.args),
                "returns": unparse_annotation(node.returns),
                "is_private": is_private,
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

    for cls in classes:
        lines.append(f"    class {cls['name']} {{")
        # Add attributes
        for attr in cls["attributes"]:
            safe_type = clean_plantuml_type(attr["type"])
            lines.append(f"        +{attr['name']}: {safe_type}")
        # Add methods
        for method in cls["methods"]:
            args_str = ", ".join(f"{arg['name']}: {clean_plantuml_type(arg['type'])}" for arg in method["args"])
            ret_str = clean_plantuml_type(method["returns"])
            lines.append(f"        +{method['name']}({args_str}) {ret_str}")
        lines.append("    }")

        # Add inheritance
        for base in cls["bases"]:
            base_name = base.split(".")[-1]
            lines.append(f"    {base_name} <|-- {cls['name']} : Generalization")

    lines.append("```")
    return "\n".join(lines)


registry = {
    'modules': {},
    'class_to_module': {},
    'function_to_module': {}
}

def build_registry(files_to_process):
    for py_file in files_to_process:
        parsed = parse_python_file(py_file)
        registry['modules'][py_file] = parsed
        for cls in parsed['classes']:
            registry['class_to_module'][cls['name']] = py_file
        for func in parsed['functions']:
            registry['function_to_module'][func['name']] = py_file

def generate_package_diagram_content():
    lines = ["```plantuml", "package \"src\" {"]
    packages = set()
    for py_file in registry['modules'].keys():
        parts = py_file.split("/")[:-1]
        pkg = ".".join(parts)
        if pkg:
            packages.add(pkg)
    for pkg in sorted(packages):
        lines.append(f"    package \"{pkg}\" {{}}")
    lines.append("}")
    lines.append("```")
    return "\n".join(lines)

def generate_dependency_graph():
    lines = ["```plantuml", "digraph Dependencies {"]
    for mod_path, data in registry['modules'].items():
        mod_name = os.path.splitext(os.path.basename(mod_path))[0]
        for imp in data['imports']:
            imp_name = imp.split('.')[-1] if '.' in imp else imp
            if imp_name != '*':
                lines.append(f"    \"{mod_name}\" -> \"{imp_name}\"")
    lines.append("}")
    lines.append("```")
    return "\n".join(lines)

def generate_markdown(parsed_data, relative_filepath):
    mod_name = os.path.splitext(os.path.basename(relative_filepath))[0]

    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    commit_hash = get_last_commit()

    # Calculate source reference path relative to openwiki/modules/ (../../)
    # The depth depends on relative_filepath
    depth = len(relative_filepath.split(os.sep)) - 1
    back_path = (
        "../" * depth + "src/" + relative_filepath.split("src/", 1)[-1]
        if "src/" in relative_filepath
        else "../../" + relative_filepath
    )

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
    body.append(f"# Module Specification: {mod_name}\n")
    body.append(f"* **Source Reference:** [{relative_filepath}]({back_path})\n")

    body.append("## 1. Architectural Role & Responsibilities")
    body.append(f"{parsed_data['docstring']}\n")

    body.append("## 2. UML 2.0 Class Diagram")
    puml = generate_plantuml(parsed_data["classes"])
    if puml:
        body.append(puml)
    else:
        body.append("_No classes found._")
    body.append("\n## 3. Class & Method Specifications\n")

    for cls in parsed_data["classes"]:
        body.append(f"### `{cls['name']}`")
        body.append(f"\n{cls['docstring']}\n")

        if cls["attributes"]:
            body.append("#### Attributes")
            for attr in cls["attributes"]:
                body.append(f"* **`{attr['name']}`** (`{attr['type']}`)")
            body.append("")

        public_methods = [m for m in cls["methods"] if not m["is_private"]]
        private_methods = [m for m in cls["methods"] if m["is_private"]]

        if public_methods:
            body.append("#### Public Methods")
            for m in public_methods:
                args_str = ", ".join(f"{arg['name']}: {arg['type']}" for arg in m["args"])
                body.append(f"* **`{m['name']}({args_str}) -> {m['returns']}`**")
                body.append(
                    f"  - **Purpose**: {m['docstring'].splitlines()[0] if m['docstring'] else 'No description available.'}"
                )
                body.append("  - **Inputs**:")
                for arg in m["args"]:
                    body.append(f"    - `{arg['name']}` (`{arg['type']}`)")
                body.append(f"  - **Outputs**: `{m['returns']}`")
            body.append("")

        if private_methods:
            body.append("#### Private Methods")
            for m in private_methods:
                args_str = ", ".join(f"{arg['name']}: {arg['type']}" for arg in m["args"])
                body.append(f"* **`{m['name']}({args_str}) -> {m['returns']}`**")
                body.append(
                    f"  - **Purpose**: {m['docstring'].splitlines()[0] if m['docstring'] else 'No description available.'}"
                )
            body.append("")

    if parsed_data["functions"]:
        body.append("## Standalone Functions\n")
        for func in parsed_data["functions"]:
            args_str = ", ".join(f"{arg['name']}: {arg['type']}" for arg in func["args"])
            body.append(f"### `{func['name']}({args_str}) -> {func['returns']}`")
            body.append(f"{func['docstring']}\n")
            body.append("#### Inputs")
            for arg in func["args"]:
                body.append(f"* `{arg['name']}` (`{arg['type']}`)")
            body.append(f"\n#### Outputs\n* `{func['returns']}`\n")

    body.append("## Dependencies\n")
    if parsed_data["imports"]:
        for imp in parsed_data["imports"]:
            body.append(f"* `{imp}`")
    else:
        body.append("_No dependencies found._")

    # Inject Used By
    used_by = []
    mod_path_dotted = relative_filepath.replace("src/", "").replace(".py", "").replace("/", ".")
    for other_py, other_data in registry['modules'].items():
        if other_py == relative_filepath:
            continue
        for imp in other_data['imports']:
            if mod_path_dotted in imp or imp.startswith(mod_name):
                used_by.append(other_py)
                break

    body.append("\n## Used By\n")
    if used_by:
        for u in sorted(used_by):
            rel_u = os.path.relpath(u, "src")[:-3] + ".md"
            depth = len(relative_filepath.split(os.sep)) - 1
            up_path = "../" * (depth - 1)
            if depth == 1:
                up_path = "./"
            body.append(f"* [{os.path.basename(u)}]({up_path}{rel_u})")
    else:
        body.append("_Not used by any other module._")

    return frontmatter + "\n".join(body) + "\n"


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
        f.write(f'---\niso_doc_type: "Description"\niso_viewpoint: "ArchitectureDescription"\ntype: "diagrams"\ntitle: "Diagrams"\ndescription: "Auto-generated architecture diagrams."\ntags: ["diagrams"]\ntimestamp: "{timestamp}"\ngenerated: "agent:ast-documentation-generator"\nverified: "true"\nlast_verified_commit: "{commit_hash}"\n---\n# Architecture Diagrams\n\n')
        f.write("## Package Diagram\n")
        f.write(generate_package_diagram_content())
        f.write("\n\n## Dependency Graph\n")
        f.write(generate_dependency_graph())

    # Build Alphabetical Index
    classes_list = sorted(list(registry['class_to_module'].keys()))
    api_list = sorted(list(registry['function_to_module'].keys()))

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
            mod = registry['class_to_module'][cls_name]
            rel_mod = os.path.relpath(mod, "src")[:-3] + ".md"
            f.write(f"* [{cls_name}](modules/{rel_mod}#{cls_name.lower()})\n")
        f.write("\n")

        f.write("## Public API index\n\n")
        for api_name in api_list:
            mod = registry['function_to_module'][api_name]
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
    for root, _, files in os.walk("src"):
        for f in files:
            if f.endswith(".py"):
                all_files.append(os.path.join(root, f))

    if args.mode == "full":
        delete_generated_docs()
        files_to_process = all_files
    else:
        files_to_process = get_changed_files()

    print(f"Mode: {args.mode}")
    print(f"Files to process: {len(files_to_process)}")

    # We must build the registry using ALL files so cross-references are complete
    build_registry(all_files)

    os.makedirs("openwiki/modules", exist_ok=True)

    for py_file in files_to_process:
        parsed = parse_python_file(py_file)

        rel_py = os.path.relpath(py_file, "src")
        md_path = os.path.join("openwiki/modules", rel_py[:-3] + ".md")

        os.makedirs(os.path.dirname(md_path), exist_ok=True)

        md_content = generate_markdown(parsed, py_file)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)

    update_index_files(files_to_process)
    print("Documentation generation complete.")

if __name__ == "__main__":
    main()
