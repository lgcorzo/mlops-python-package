import os
import sys
import ast
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

IGNORE_DIRS = {".git", ".github", ".vscode", ".idea", "node_modules", "dist", "bin", "obj", "target", "coverage", "__pycache__", "openwiki"}

def get_git_diff_files():
    try:
        result = subprocess.run(["git", "diff", "--name-only"], capture_output=True, text=True)
        files = result.stdout.strip().split('\n')

        result_cached = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True)
        files += result_cached.stdout.strip().split('\n')

        if not any(files):
            res_head = subprocess.run(["git", "diff", "HEAD~1", "HEAD", "--name-only"], capture_output=True, text=True)
            files += res_head.stdout.strip().split('\n')

        return [f for f in set(files) if f and f.endswith('.py') and os.path.exists(f)]
    except Exception:
        return []

def extract_type(annotation):
    if annotation is None:
        return "Any"
    return ast.unparse(annotation)

def parse_docstring_tags(docstring, tag):
    """Simple parser to find things like Time O(N) or Side Effects: ... in docstrings."""
    if not docstring:
        return "Not documented"

    lines = docstring.split('\n')
    for i, line in enumerate(lines):
        if tag.lower() in line.lower():
            return line.strip()
    return "Not documented"

def extract_complexity(docstring):
    return parse_docstring_tags(docstring, "complexity")

def extract_side_effects(docstring):
    return parse_docstring_tags(docstring, "side effect")

def parse_class(node):
    cls_info = {
        "name": node.name,
        "bases": [ast.unparse(b) for b in node.bases],
        "docstring": ast.get_docstring(node) or "No description available.",
        "methods": [],
        "attributes": [],
        "constructor": None
    }

    for body_item in node.body:
        if isinstance(body_item, ast.FunctionDef):
            method_info = parse_function(body_item)
            if body_item.name == "__init__":
                cls_info["constructor"] = method_info
            else:
                cls_info["methods"].append(method_info)
        elif isinstance(body_item, ast.AnnAssign):
            if isinstance(body_item.target, ast.Name):
                cls_info["attributes"].append({
                    "name": body_item.target.id,
                    "type": extract_type(body_item.annotation),
                    "doc": ""
                })
        elif isinstance(body_item, ast.Assign):
            for target in body_item.targets:
                if isinstance(target, ast.Name):
                    cls_info["attributes"].append({
                        "name": target.id,
                        "type": "Any",
                        "doc": ""
                    })
    return cls_info

def parse_function(node):
    func_info = {
        "name": node.name,
        "is_private": node.name.startswith("_") and node.name != "__init__",
        "docstring": ast.get_docstring(node) or "No description available.",
        "args": [],
        "returns": extract_type(node.returns),
        "calls": []
    }
    for arg in node.args.args:
        func_info["args"].append({
            "name": arg.arg,
            "type": extract_type(arg.annotation)
        })

    for subnode in ast.walk(node):
        if isinstance(subnode, ast.Call):
            if isinstance(subnode.func, ast.Name):
                func_info["calls"].append(subnode.func.id)
            elif isinstance(subnode.func, ast.Attribute):
                func_info["calls"].append(subnode.func.attr)

    func_info["complexity"] = extract_complexity(func_info["docstring"])
    func_info["side_effects"] = extract_side_effects(func_info["docstring"])

    return func_info

def parse_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source)
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return None

    module_info = {
        "filepath": filepath,
        "docstring": ast.get_docstring(tree) or "Module providing various functionalities.",
        "imports": [],
        "classes": [],
        "functions": [],
        "exports": []
    }

    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                module_info["imports"].append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                module_info["imports"].append(node.module)
        elif isinstance(node, ast.ClassDef):
            cls_info = parse_class(node)
            module_info["classes"].append(cls_info)
            if not node.name.startswith("_"):
                module_info["exports"].append(node.name)
        elif isinstance(node, ast.FunctionDef):
            func_info = parse_function(node)
            module_info["functions"].append(func_info)
            if not node.name.startswith("_"):
                module_info["exports"].append(node.name)

    return module_info

def generate_plantuml_class(cls_info):
    lines = [f"class {cls_info['name']} {{"]
    for attr in cls_info["attributes"]:
        lines.append(f"  +{attr['name']} : {attr['type']}")
    if cls_info["constructor"]:
        args = ", ".join([f"{a['name']}:{a['type']}" for a in cls_info["constructor"]["args"]])
        lines.append(f"  +__init__({args})")
    for m in cls_info["methods"]:
        prefix = "-" if m["is_private"] else "+"
        args = ", ".join([f"{a['name']}:{a['type']}" for a in m["args"]])
        lines.append(f"  {prefix}{m['name']}({args}) : {m['returns']}")
    lines.append("}")
    for base in cls_info["bases"]:
        lines.append(f"{base} <|-- {cls_info['name']}")
    return "\n".join(lines)

def detect_architecture(filepath):
    filepath = filepath.lower()
    if "controller" in filepath or "api" in filepath:
        return "Controllers"
    if "service" in filepath:
        return "Services"
    if "schema" in filepath or "dto" in filepath:
        return "DTOs"
    if "model" in filepath or "entity" in filepath:
        return "Domain Models"
    if "repository" in filepath or "db" in filepath:
        return "Repositories"
    return "Infrastructure"

def generate_markdown(module_info):
    filepath = module_info["filepath"]
    name = Path(filepath).stem
    arch_role = detect_architecture(filepath)

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    md = f"""---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "{name} Documentation"
description: "Documentation for {filepath}"
tags: ["module", "{name}"]
timestamp: "{timestamp}"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `{filepath}`

## Overview
**Purpose**: {module_info['docstring'].splitlines()[0] if module_info['docstring'] else 'Provides specific functionality for the application.'}

**Architecture Role**: {arch_role}

**Dependencies**:
"""
    for imp in set(module_info["imports"]):
        md += f"- `{imp}`\n"

    md += "\n**Exported Symbols**:\n"
    for exp in module_info["exports"]:
        md += f"- `{exp}`\n"

    md += "\n## UML Class Diagram\n```plantuml\n@startuml\n"
    for cls in module_info["classes"]:
        md += generate_plantuml_class(cls) + "\n"
    md += "@enduml\n```\n\n"

    md += "## Call Graph\n```plantuml\n@startuml\n"
    for func in module_info["functions"]:
        for call in func["calls"]:
            md += f"{func['name']} --> {call}\n"
    for cls in module_info["classes"]:
        for m in cls["methods"]:
            for call in m["calls"]:
                md += f"{cls['name']}::{m['name']} --> {call}\n"
    md += "@enduml\n```\n\n"

    md += "## Classes\n"
    for cls in module_info["classes"]:
        md += f"### Class `{cls['name']}`\n"
        md += f"**Overview**: {cls['docstring']}\n\n"

        if cls["constructor"]:
            md += "#### Constructor\n"
            for arg in cls["constructor"]["args"]:
                md += f"- `{arg['name']}` ({arg['type']})\n"

        if cls["attributes"]:
            md += "#### Attributes\n"
            for attr in cls["attributes"]:
                md += f"- `{attr['name']}`: {attr['type']}\n"

        md += "#### Public Methods\n"
        for m in cls["methods"]:
            if not m["is_private"]:
                md += f"##### `{m['name']}`\n"
                md += f"- **Description**: {m['docstring']}\n"
                md += "- **Inputs**:\n"
                for arg in m["args"]:
                    md += f"  - `{arg['name']}`: {arg['type']}\n"
                md += f"- **Output**: `{m['returns']}`\n"
                md += f"- **Side Effects**: {m['side_effects']}\n"
                md += f"- **Complexity**: {m['complexity']}\n\n"

        md += "#### Private Methods\n"
        for m in cls["methods"]:
            if m["is_private"]:
                md += f"##### `{m['name']}`\n"
                md += f"- **Purpose**: {m['docstring']}\n"
                md += f"- **Parameters**: {', '.join([a['name'] for a in m['args']])}\n"
                md += f"- **Return**: `{m['returns']}`\n\n"

    md += "## Functions\n"
    for func in module_info["functions"]:
        md += f"### Function `{func['name']}`\n"
        md += f"- **Description**: {func['docstring']}\n"
        md += "- **Inputs**:\n"
        for arg in func["args"]:
            md += f"  - `{arg['name']}`: {arg['type']}\n"
        md += f"- **Output**: `{func['returns']}`\n"
        md += f"- **Side Effects**: {func['side_effects']}\n"
        md += f"- **Complexity**: {func['complexity']}\n\n"

    return md

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def setup_openwiki_structure():
    base_dir = "openwiki"
    folders = ["architecture", "modules", "api", "classes", "diagrams", "dependencies", "glossary", "decisions", "generated"]
    for folder in folders:
        os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

def generate_global_diagrams(modules):
    # Package diagram
    pkg_diagram = "```plantuml\n@startuml\n"
    packages = set()
    for m in modules:
        parts = Path(m["filepath"]).parts[:-1]
        for i in range(1, len(parts) + 1):
            packages.add("/".join(parts[:i]))
    for pkg in sorted(packages):
        pkg_diagram += f"package \"{pkg}\" {{}}\n"
    pkg_diagram += "@enduml\n```\n"
    write_file("openwiki/diagrams/package_diagram.md", f"# Package Diagram\n\n{pkg_diagram}")

    # Dependency diagram
    dep_diagram = "```plantuml\n@startuml\n"
    for m in modules:
        source_pkg = "/".join(Path(m["filepath"]).parts[:-1]) or "root"
        for imp in m["imports"]:
            target_pkg = imp.replace(".", "/")
            dep_diagram += f"\"{source_pkg}\" --> \"{target_pkg}\"\n"
    dep_diagram += "@enduml\n```\n"
    write_file("openwiki/diagrams/dependency_graph.md", f"# Dependency Graph\n\n{dep_diagram}")

def generate_architecture(modules):
    arch = {}
    for m in modules:
        role = detect_architecture(m["filepath"])
        if role not in arch:
            arch[role] = []
        arch[role].append(m["filepath"])

    md = "# Architectural Overview\n\n"
    for role, files in arch.items():
        md += f"## {role}\n"
        for f in files:
            md_path = f.replace(".py", ".md")
            md += f"- [{f}]({md_path})\n"
    write_file("openwiki/architecture/overview.md", md)

def generate_summary(modules):
    summary = "# SUMMARY\n\n## Table of Contents\n\n### Architecture\n- [Overview](architecture/overview.md)\n"
    summary += "- [Package Diagram](diagrams/package_diagram.md)\n"
    summary += "- [Dependency Graph](diagrams/dependency_graph.md)\n\n"
    summary += "### Modules\n"
    for m in sorted(modules, key=lambda x: x["filepath"]):
        md_path = m["filepath"].replace(".py", ".md")
        # Ensure path is relative
        md_path = md_path if not md_path.startswith("openwiki/") else md_path[9:]
        summary += f"- [{m['filepath']}]({md_path})\n"

    summary += "\n### Classes\n"
    classes = []
    for m in modules:
        for c in m["classes"]:
            md_path = m["filepath"].replace(".py", ".md")
            md_path = md_path if not md_path.startswith("openwiki/") else md_path[9:]
            classes.append(f"- [{c['name']}]({md_path}#{c['name'].lower()})")
    for c in sorted(classes):
        summary += c + "\n"

    write_file("openwiki/SUMMARY.md", summary)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_openwiki.py <mode>")
        sys.exit(1)

    mode = sys.argv[1].lower()

    if mode == "full":
        if os.path.exists("openwiki"):
            shutil.rmtree("openwiki")
        os.makedirs("openwiki")

        setup_openwiki_structure()

        all_modules = []
        for root, dirs, files in os.walk("."):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith(".")]
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(root, file)
                    if filepath.startswith("./"):
                        filepath = filepath[2:]
                    module_info = parse_file(filepath)
                    if module_info:
                        all_modules.append(module_info)
                        md_content = generate_markdown(module_info)
                        out_path = os.path.join("openwiki", filepath.replace(".py", ".md"))
                        write_file(out_path, md_content)

        generate_summary(all_modules)
        generate_global_diagrams(all_modules)
        generate_architecture(all_modules)

        # create index.md
        index_md = f"""---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "hub"
title: "OpenWiki Master Knowledge Hub"
description: "Master index and navigation hub"
tags: ["index", "navigation", "okf"]
timestamp: "{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# OpenWiki Master Knowledge Hub

Welcome to the **ISO/IEC/IEEE Standard OpenWiki Documentation Hub**.
Please see the [SUMMARY](SUMMARY.md) for navigation.
"""
        write_file("openwiki/index.md", index_md)

    elif mode == "diff":
        setup_openwiki_structure()
        changed_files = get_git_diff_files()
        all_modules = []
        for root, dirs, files in os.walk("."):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith(".")]
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(root, file)
                    if filepath.startswith("./"):
                        filepath = filepath[2:]

                    if filepath in changed_files:
                        module_info = parse_file(filepath)
                        if module_info:
                            all_modules.append(module_info)
                            md_content = generate_markdown(module_info)
                            out_path = os.path.join("openwiki", filepath.replace(".py", ".md"))
                            write_file(out_path, md_content)
                    else:
                        # just parse to keep in summary
                        module_info = parse_file(filepath)
                        if module_info:
                            all_modules.append(module_info)

        generate_summary(all_modules)
        generate_global_diagrams(all_modules)
        generate_architecture(all_modules)
        print(f"Updated docs for: {changed_files}")
    else:
        print(f"Unknown mode: {mode}")

if __name__ == "__main__":
    main()
