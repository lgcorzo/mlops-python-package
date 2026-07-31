#!/usr/bin/env python3
import os
import re
import glob

def camel_to_snake(name):
    # Handle special cases
    if name.lower() == 'init':
        return '__init__'
    if name.lower() == 'main':
        return '__main__'
    # Standard camel to snake
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def resolve_wiki_link(link_content, current_file_dir, wiki_root):
    # Split by /
    parts = link_content.split('/')
    normalized_parts = []
    for part in parts:
        # Convert each part from CamelCase to snake_case
        normalized_parts.append(camel_to_snake(part))
    
    relative_target = "/".join(normalized_parts) + ".md"
    target_abs_path = os.path.normpath(os.path.join(wiki_root, relative_target))
    
    if os.path.exists(target_abs_path):
        # Calculate relative path from current_file_dir to target_abs_path
        rel_path = os.path.relpath(target_abs_path, current_file_dir)
        return rel_path
    
    # Try case-insensitive search or exact file existence check if the above normalization failed
    # Let's walk the wiki_root to find a match for the base name
    target_base = normalized_parts[-1]
    for root, dirs, files in os.walk(wiki_root):
        for f in files:
            f_base = os.path.splitext(f)[0]
            if f_base.lower() == target_base.lower() or f_base.lower() == camel_to_snake(parts[-1]).lower():
                rel_path = os.path.relpath(os.path.join(root, f), current_file_dir)
                return rel_path
                
    return None

def convert_file(file_path, wiki_root):
    current_file_dir = os.path.dirname(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Convert [[WikiLinks]] to [WikiLinks](relative_path)
    # Match [[link]] or [[link|label]]
    wiki_pattern = re.compile(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]')
    
    def replace_wiki(match):
        link_content = match.group(1).strip()
        label = match.group(2) if match.group(2) else link_content
        
        # Resolve target
        rel_path = resolve_wiki_link(link_content, current_file_dir, wiki_root)
        if rel_path:
            return f"[{label}]({rel_path})"
        else:
            # Keep as is if not resolved
            return match.group(0)
            
    content = wiki_pattern.sub(replace_wiki, content)
    
    # 2. Convert (src/path/to/file.py:L1-L10) to [src/path/to/file.py:L1-L10](../src/path/to/file.py#L1-L10)
    # relative to the repo root.
    repo_root = os.path.dirname(wiki_root)
    
    src_pattern = re.compile(r'\b(src/[a-zA-Z0-9_\-\./]+(?::L\d+(?:-L\d+)?)?)\b')
    
    def replace_src(match):
        full_ref = match.group(1)
        # Split by line numbers if present
        parts = full_ref.split(':')
        file_rel_path = parts[0]
        line_anchor = ""
        if len(parts) > 1:
            line_anchor = "#" + parts[1]
            
        file_abs_path = os.path.join(repo_root, file_rel_path)
        if os.path.exists(file_abs_path):
            # Calculate relative path from current_file_dir to file_abs_path
            rel_path = os.path.relpath(file_abs_path, current_file_dir)
            return f"[{full_ref}]({rel_path}{line_anchor})"
        return full_ref

    content = src_pattern.sub(replace_src, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    wiki_root = os.path.abspath("openwiki")
    if not os.path.exists(wiki_root):
        print("Error: openwiki folder not found in current directory.")
        return
        
    md_files = glob.glob(os.path.join(wiki_root, "**", "*.md"), recursive=True)
    print(f"Converting links in {len(md_files)} files...")
    for file_path in md_files:
        convert_file(file_path, wiki_root)
    print("Done!")

if __name__ == "__main__":
    main()
