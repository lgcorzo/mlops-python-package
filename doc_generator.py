import ast
import os
import re
import subprocess
from pathlib import Path


def get_git_commit():
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode("utf-8").strip()
    except Exception:
        return "unknown"


def get_changed_files():
    last_verified_commit = None
    try:
        import glob
        import re

        for f in glob.glob("wiki/*.md"):
            with open(f, "r") as fp:
                c = fp.read()
                match = re.search(r'last_verified_commit: "([^"]+)"', c)
                if match:
                    last_verified_commit = match.group(1)
                    break
    except Exception:
        pass

    if last_verified_commit:
        try:
            output = subprocess.check_output(
                ["git", "diff", last_verified_commit, "HEAD", "--name-only"], stderr=subprocess.STDOUT
            ).decode("utf-8")
            res = [f for f in output.split("\n") if f.startswith("src/") and f.endswith(".py")]
            return res
        except subprocess.CalledProcessError:
            pass

    try:
        output = subprocess.check_output(
            ["git", "show", "--name-only", "--format=", "HEAD"], stderr=subprocess.STDOUT
        ).decode("utf-8")
        res = [f for f in output.split("\n") if f.startswith("src/") and f.endswith(".py")]
        return res
    except subprocess.CalledProcessError:
        pass

    return []


class ClassVisitor(ast.NodeVisitor):
    def __init__(self):
        self.classes = []
        self.current_class_path = []

    def visit_ClassDef(self, node):
        class_name = node.name
        if self.current_class_path:
            class_name = f"{'.'.join(self.current_class_path)}.{class_name}"

        class_info = {
            "name": class_name,
            "bases": [b.id for b in node.bases if isinstance(b, ast.Name)],
            "methods": [],
            "attributes": [],
        }

        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                args = []
                for a in item.args.args:
                    if a.arg != "self":
                        args.append(f"{a.arg}")

                return_annotation = ""
                if item.returns:
                    if isinstance(item.returns, ast.Name):
                        return_annotation = f" : {item.returns.id}"
                    elif isinstance(item.returns, ast.Constant) and item.returns.value is None:
                        return_annotation = " : None"
                    elif isinstance(item.returns, ast.Subscript) and isinstance(item.returns.value, ast.Name):
                        if hasattr(item.returns.slice, "id"):
                            return_annotation = f" : {item.returns.value.id}[{item.returns.slice.id}]"
                        else:
                            return_annotation = f" : {item.returns.value.id}"
                    else:
                        return_annotation = " : Any"

                class_info["methods"].append(f"{item.name}({', '.join(args)}){return_annotation}")
            elif isinstance(item, ast.AnnAssign):
                if isinstance(item.target, ast.Name):
                    class_info["attributes"].append(item.target.id)
            elif isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name):
                        class_info["attributes"].append(target.id)

        self.classes.append(class_info)

        self.current_class_path.append(node.name)
        self.generic_visit(node)
        self.current_class_path.pop()


def parse_ast(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    tree = ast.parse(content)

    visitor = ClassVisitor()
    visitor.visit(tree)
    classes = visitor.classes

    imports = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module.replace(".", "_"))

    return classes, sorted(list(set(imports)))


def generate_class_diagram(classes):
    if not classes:
        return ""

    lines = ["```mermaid", "classDiagram"]
    for cls in classes:
        lines.append(f"    class {cls['name']} {{")
        for attr in cls["attributes"]:
            prefix = "+" if not attr.startswith("_") else ("-" if attr.startswith("__") else "#")
            lines.append(f"        {prefix}{attr}")
        for method in cls["methods"]:
            prefix = "+" if not method.startswith("_") else ("-" if method.startswith("__") else "#")
            if method.startswith("__") and method.endswith("__"):
                prefix = "+"
            lines.append(f"        {prefix}{method}")
        lines.append("    }")
        for base in cls["bases"]:
            lines.append(f"    {base} <|-- {cls['name']}")
    lines.append("```")
    return "\n".join(lines)


def generate_flowchart(module_name, imports):
    lines = ["```mermaid", "flowchart TD"]
    if not imports:
        lines.append("    A[No Classes/Dependencies found] --> B[End]")
    else:
        for imp in imports:
            lines.append(f"    {module_name} --> {imp}")
    lines.append("```")
    return "\n".join(lines)


def extract_block(body, regex_pattern):
    match = re.search(regex_pattern, body, flags=re.DOTALL)
    if match:
        return match.group(0)
    return ""


def process_file(filepath, commit_hash):
    path = Path(filepath)
    if path.name == "__init__.py":
        md_name = f"{path.parent.name}_init"
    else:
        md_name = path.stem

    md_filepath = Path("wiki") / f"{md_name}.md"

    classes, imports = parse_ast(filepath)
    class_diagram = generate_class_diagram(classes)
    flowchart = generate_flowchart(md_name, imports)

    changed = False

    if md_filepath.exists():
        with open(md_filepath, "r") as f:
            original_content = f.read()
            content = original_content

        if "---" in content:
            frontmatter_end = content.find("---", 3)
            if frontmatter_end != -1:
                frontmatter = content[: frontmatter_end + 3]
                body = content[frontmatter_end + 3 :]

                # We MUST explicitly include its project-relative path directly underneath the title
                source_file_match = re.search(r"^Source File: .*$", body, re.MULTILINE)
                if not source_file_match:
                    title_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
                    if title_match:
                        insert_pos = title_match.end() + 1
                        body = body[:insert_pos] + f"\n\nSource File: `{filepath}`" + body[insert_pos:]
                        changed = True

                if class_diagram:
                    if "```mermaid\nclassDiagram" in body:
                        existing_diagram = extract_block(body, r"```mermaid\nclassDiagram.*?```")
                        if existing_diagram != class_diagram:
                            body = re.sub(r"```mermaid\nclassDiagram.*?```", class_diagram, body, flags=re.DOTALL)
                            changed = True
                    else:
                        body += f"\n\n{class_diagram}"
                        changed = True

                if flowchart:
                    if "```mermaid\nflowchart TD" in body:
                        parts = body.split("```mermaid\nflowchart TD")
                        if len(parts) > 1:
                            for i in range(1, len(parts)):
                                end_idx = parts[i].find("```")
                                block_content = parts[i][:end_idx]
                                # Heuristic: the auto-generated one has NO subgraph and NO |
                                if (
                                    "subgraph " not in block_content
                                    and "|" not in block_content
                                    and (
                                        " abc" in block_content
                                        or "typing" in block_content
                                        or "pydantic" in block_content
                                        or (md_name + " -->") in block_content
                                        or "Dependencies found" in block_content
                                    )
                                ):
                                    new_block = flowchart[23:] + parts[i][end_idx + 3 :]
                                    if parts[i] != new_block:
                                        parts[i] = new_block
                                        changed = True
                                    break
                            else:
                                body += f"\n\n{flowchart}"
                                changed = True
                                parts = None
                            if parts:
                                body = "```mermaid\nflowchart TD".join(parts)
                    else:
                        body += f"\n\n{flowchart}"
                        changed = True

                body = re.sub(r"\n{3,}", "\n\n", body)

                if changed:
                    frontmatter = re.sub(
                        r"last_verified_commit:.*", f'last_verified_commit: "{commit_hash}"', frontmatter
                    )
                    content = frontmatter + body
    else:
        changed = True
        title = md_name
        content = f"""---
type: script
title: "{title}"
source_path: "{filepath}"
description: "Documentation for {filepath}"
tags: [script]
last_verified_commit: "{commit_hash}"
---

# {title}

Source File: `{filepath}`

{class_diagram}

{flowchart}
"""

    if changed:
        with open(md_filepath, "w") as f:
            f.write(content)
        return md_name
    return None


def update_index(modules):
    index_path = Path("wiki/index.md")
    if not index_path.exists():
        return

    with open(index_path, "r") as f:
        content = f.read()

    header = "## Source Code Documentation"

    if header in content:
        parts = content.split(header)
        pre_header = parts[0]

        links = "\n".join([f"- [[{mod}]]" for mod in sorted(modules)])
        new_content = f"{pre_header}{header}\n\n{links}\n"

        if new_content != content:
            with open(index_path, "w") as f:
                f.write(new_content)


def main():
    commit_hash = get_git_commit()
    changed_files = get_changed_files()

    modules = []

    if changed_files:
        for filepath in changed_files:
            if os.path.exists(filepath):
                mod_name = process_file(filepath, commit_hash)
                if mod_name:
                    modules.append(mod_name)
    else:
        print("No changed files found in src/ or code/ directories.")

    if modules:
        # We always ensure index links are correct for all files if we touch any
        all_modules = []
        for root, _, files in os.walk("src"):
            for file in files:
                if file.endswith(".py"):
                    path = Path(os.path.join(root, file))
                    if path.name == "__init__.py":
                        all_modules.append(f"{path.parent.name}_init")
                    else:
                        all_modules.append(path.stem)

        update_index(all_modules)
    print(f"Processed {len(modules)} changed files.")


if __name__ == "__main__":
    main()
