import argparse
import ast
import glob
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from typing import Any, Dict, List, Tuple

IGNORE_DIRS = {
    ".git", ".github", ".vscode", ".idea", "node_modules",
    "dist", "bin", "obj", "target", "coverage", "__pycache__"
}

def get_git_commit() -> str:
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD'], stderr=subprocess.DEVNULL).decode('utf-8').strip()
    except Exception:
        return "unknown"

def get_changed_files() -> List[str]:
    try:
        output = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD'], stderr=subprocess.DEVNULL).decode('utf-8')
        return [line.strip() for line in output.splitlines() if line.strip() and line.endswith('.py')]
    except Exception:
        return []

def get_all_files() -> List[str]:
    files = []
    for root, dirs, filenames in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith('.')]
        for f in filenames:
            if f.endswith('.py'):
                norm = os.path.normpath(os.path.join(root, f))
                if norm.startswith('src/'):
                    files.append(norm)
    return files

def parse_existing_frontmatter_and_content(md_path: str) -> Tuple[Dict[str, str], str]:
    if not os.path.exists(md_path):
        return {}, ""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content

    yaml_lines = parts[1].strip().split('\n')
    fm = {}
    for line in yaml_lines:
        if ':' in line:
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")

    return fm, parts[2]

def get_ast_info(filepath: str) -> Dict[str, Any]:
    with open(filepath, 'r', encoding='utf-8') as f:
        source = f.read()

    try:
        tree = ast.parse(source)
    except Exception:
        return None

    info = {
        'imports': [],
        'classes': [],
        'functions': [],
        'docstring': ast.get_docstring(tree)
    }

    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                info['imports'].append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                info['imports'].append(node.module)
        elif isinstance(node, ast.ClassDef):
            cls_info = {
                'name': node.name,
                'docstring': ast.get_docstring(node),
                'bases': [b.id for b in node.bases if isinstance(b, ast.Name)],
                'methods': [],
                'attributes': []
            }
            for cnode in node.body:
                if isinstance(cnode, ast.FunctionDef) or isinstance(cnode, ast.AsyncFunctionDef):
                    meth_info = {
                        'name': cnode.name,
                        'docstring': ast.get_docstring(cnode),
                        'args': [arg.arg for arg in cnode.args.args],
                        'returns': ast.unparse(cnode.returns) if cnode.returns else "None",
                    }
                    cls_info['methods'].append(meth_info)
                elif isinstance(cnode, ast.AnnAssign):
                    if isinstance(cnode.target, ast.Name):
                        cls_info['attributes'].append(cnode.target.id)
                elif isinstance(cnode, ast.Assign):
                    for t in cnode.targets:
                        if isinstance(t, ast.Name):
                            cls_info['attributes'].append(t.id)
            info['classes'].append(cls_info)
        elif isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
            func_info = {
                'name': node.name,
                'docstring': ast.get_docstring(node),
                'args': [arg.arg for arg in node.args.args],
                'returns': ast.unparse(node.returns) if node.returns else "None",
            }
            info['functions'].append(func_info)

    return info

def generate_plantuml(info: dict, module_name: str) -> str:
    lines = ["```plantuml", "@startuml"]
    for cls in info['classes']:
        lines.append(f"class {cls['name']} {{")
        for attr in cls['attributes']:
            lines.append(f"  +{attr}")
        for meth in cls['methods']:
            args = ", ".join(meth['args'])
            lines.append(f"  +{meth['name']}({args})")
        lines.append("}")
        for base in cls['bases']:
            lines.append(f"{base} <|-- {cls['name']}")
    lines.append("@enduml")
    lines.append("```")
    return "\n".join(lines)

def generate_markdown(filepath: str, info: dict, existing_fm: dict, existing_body: str) -> str:
    fm = existing_fm.copy()
    fm['type'] = fm.get('type', 'Concept')
    fm['title'] = fm.get('title', filepath)
    fm['description'] = fm.get('description', f"Documentation for {filepath}")

    # Handle tags specifically
    if 'tags' not in fm:
        fm['tags'] = '[ast, python, auto-generated]'
    elif isinstance(fm['tags'], str) and not fm['tags'].startswith('['):
        fm['tags'] = f"[{fm['tags']}]"

    fm['timestamp'] = datetime.now().isoformat()
    fm['iso_doc_type'] = fm.get('iso_doc_type', 'Description')
    fm['iso_viewpoint'] = fm.get('iso_viewpoint', 'ArchitectureDescription')
    fm['generated'] = 'true'
    fm['verified'] = 'false'
    fm['last_verified_commit'] = get_git_commit()

    content = ["---"]
    for k, v in fm.items():
        if k == 'tags' and str(v).startswith('['):
            content.append(f"{k}: {v}")
        elif k in ('generated', 'verified'):
            content.append(f"{k}: {v}")
        else:
            val = str(v)
            if val.startswith('"') and val.endswith('"'):
                content.append(f"{k}: {val}")
            else:
                content.append(f"{k}: \"{val}\"")
    content.append("---")
    content.append("")

    # Body generation with specific idempotency constraints
    auto_content = []
    auto_content.append(f"# {filepath}")
    auto_content.append("")

    if info.get('docstring'):
        auto_content.append("## Module Overview")
        auto_content.append(info['docstring'])
        auto_content.append("")

    auto_content.append("## Dependencies")
    if info['imports']:
        for imp in info['imports']:
            auto_content.append(f"- `{imp}`")
    else:
        auto_content.append("None")
    auto_content.append("")

    auto_content.append("## Public API")
    if info['functions']:
        for func in info['functions']:
            if not func['name'].startswith('_'):
                auto_content.append(f"### Function `{func['name']}`")
                if func['docstring']:
                    auto_content.append(func['docstring'])
                auto_content.append(f"- **Arguments:** {', '.join(func['args'])}")
                auto_content.append(f"- **Returns:** {func['returns']}")
                auto_content.append("")

    auto_content.append("## Classes")
    for cls in info['classes']:
        auto_content.append(f"### Class `{cls['name']}`")
        if cls['docstring']:
            auto_content.append(cls['docstring'])
        auto_content.append(f"- **Bases:** {', '.join(cls['bases']) if cls['bases'] else 'None'}")
        auto_content.append("")
        auto_content.append("#### Attributes")
        if cls['attributes']:
            for attr in cls['attributes']:
                auto_content.append(f"- `{attr}`")
        else:
            auto_content.append("None")
        auto_content.append("")
        auto_content.append("#### Methods")
        for meth in cls['methods']:
            auto_content.append(f"##### `{meth['name']}`")
            if meth['docstring']:
                auto_content.append(meth['docstring'])
            auto_content.append(f"- **Arguments:** {', '.join(meth['args'])}")
            auto_content.append(f"- **Returns:** {meth['returns']}")
            auto_content.append("")

    auto_content.append("## UML")

    custom_uml = ""
    if "```plantuml" in existing_body and "## UML" in existing_body:
        uml_match = re.search(r'```plantuml\s*@startuml(.*?)@enduml\s*```', existing_body, re.DOTALL)
        if uml_match and "AUTOGENERATED_START" not in existing_body:
            custom_uml = uml_match.group(0)

    if custom_uml:
        auto_content.append(custom_uml)
    else:
        auto_content.append(generate_plantuml(info, filepath))

    auto_text = "\n".join(auto_content)

    body = []
    if existing_body.strip():
        if "<!-- AUTOGENERATED_START -->" in existing_body and "<!-- AUTOGENERATED_END -->" in existing_body:
            new_body = re.sub(
                r'<!-- AUTOGENERATED_START -->.*?<!-- AUTOGENERATED_END -->',
                f'<!-- AUTOGENERATED_START -->\n{auto_text}\n<!-- AUTOGENERATED_END -->',
                existing_body,
                flags=re.DOTALL
            )
            body.append(new_body.strip())
        else:
            body.append("<!-- AUTOGENERATED_START -->")
            body.append(auto_text)
            body.append("<!-- AUTOGENERATED_END -->")
            # Avoid appending existing body to prevent duplicated headers if it already contains them but without tags
    else:
        body.append("<!-- AUTOGENERATED_START -->")
        body.append(auto_text)
        body.append("<!-- AUTOGENERATED_END -->")

    final_str = "\n".join(content) + "\n" + "\n".join(body)
    return final_str + "\n"

def write_documentation(filepath: str, out_path: str, mode: str):
    info = get_ast_info(filepath)
    if info is None:
        return

    existing_fm, existing_body = {}, ""
    if mode == 'diff' and os.path.exists(out_path):
        existing_fm, existing_body = parse_existing_frontmatter_and_content(out_path)

    new_content = generate_markdown(filepath, info, existing_fm, existing_body)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def get_out_path(filepath: str):
    base = os.path.splitext(filepath)[0]
    # Remove 'src/' and prepend 'openwiki/modules/'
    if base.startswith('src/'):
        base = base[4:]
    return os.path.join("openwiki", "modules", base + ".md")

def create_reserved_file(filename: str, title: str):
    out_path = os.path.join("openwiki", filename)
    content = [
        "---",
        "type: Concept",
        f"title: \"{title}\"",
        f"description: \"{title}\"",
        "tags: [system]",
        f"timestamp: \"{datetime.now().isoformat()}\"",
        "iso_doc_type: Description",
        "iso_viewpoint: ArchitectureDescription",
        "generated: true",
        "verified: false",
        f"last_verified_commit: \"{get_git_commit()}\"",
        "---",
        "",
        f"# {title}",
        ""
    ]
    os.makedirs("openwiki", exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(content))

def parse_args():
    mode = 'full'
    for arg in sys.argv[1:]:
        if arg == 'mode=full':
            mode = 'full'
        elif arg == 'mode=diff':
            mode = 'diff'
        elif arg == '--mode':
            pass
        elif arg in ['full', 'diff']:
            mode = arg
    return mode

def main():
    mode = parse_args()

    if mode == 'full':
        if os.path.exists('openwiki'):
            for item in os.listdir('openwiki'):
                if item == 'logs.md':
                    continue
                item_path = os.path.join('openwiki', item)
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)

        files = get_all_files()
        for f in files:
            out_path = get_out_path(f)
            write_documentation(f, out_path, mode)


        folders = ['architecture', 'modules', 'api', 'classes', 'diagrams', 'dependencies', 'glossary', 'decisions', 'generated']
        for f in folders:
            os.makedirs(os.path.join('openwiki', f), exist_ok=True)

        create_reserved_file("index.md", "OpenWiki Index")

        # Build SUMMARY.md
        summary_content = [
            "---",
            "type: Concept",
            "title: \"Summary\"",
            "description: \"Navigation Summary\"",
            "tags: [system, summary]",
            f"timestamp: \"{datetime.now().isoformat()}\"",
            "iso_doc_type: Description",
            "iso_viewpoint: ArchitectureDescription",
            "generated: true",
            "verified: false",
            f"last_verified_commit: \"{get_git_commit()}\"",
            "---",
            "",
            "# Table of Contents",
            "",
            "## Modules"
        ]
        for f in files:
            md_path = get_out_path(f)
            rel_path = os.path.relpath(md_path, "openwiki")
            summary_content.append(f"- [{os.path.basename(f)}]({rel_path})")

        summary_content.append("")
        summary_content.append("## Architecture")
        summary_content.append("- [Index](index.md)")

        with open("openwiki/SUMMARY.md", "w") as f:
            f.write("\n".join(summary_content))

        # Add a dummy package diagram placeholder
        pkg_content = [
            "---",
            "type: Concept",
            "title: \"Package Diagram\"",
            "description: \"Package Diagram\"",
            "tags: [system, diagram]",
            f"timestamp: \"{datetime.now().isoformat()}\"",
            "iso_doc_type: Description",
            "iso_viewpoint: ArchitectureDescription",
            "generated: true",
            "verified: false",
            f"last_verified_commit: \"{get_git_commit()}\"",
            "---",
            "",
            "# Package Diagram",
            "",
            "```plantuml",
            "@startuml",
            "package \"src\" {",
            "}",
            "@enduml",
            "```"
        ]
        with open("openwiki/diagrams/packages.md", "w") as f:
            f.write("\n".join(pkg_content))



    elif mode == 'diff':
        files = get_changed_files()
        for f in files:
            if f.startswith('src/'):
                out_path = get_out_path(f)
                write_documentation(f, out_path, mode)

if __name__ == "__main__":
    main()
