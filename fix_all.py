import os
import re

def fix():
    for root, _, files in os.walk('wiki'):
        for file in files:
            if file.endswith('.md') and not file in ['index.md', 'log.md', '_Sidebar.md']:
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    content = f.read()

                # Enforce the string "Source File: `path/to/script.py`" if it's a script documentation file
                # The rule says: "Every document created or updated for a script or class must explicitly include its project-relative path directly underneath the title"

                if 'type: script' in content or 'type: class' in content:
                    source_path_match = re.search(r'^source_path:\s+"(.*?)"$', content, re.MULTILINE)
                    if source_path_match:
                         source_path = source_path_match.group(1)

                         if f"Source File: `{source_path}`" not in content:
                             title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                             if title_match:
                                 insert_pos = title_match.end() + 1
                                 content = content[:insert_pos] + f"\n\nSource File: `{source_path}`" + content[insert_pos:]

                                 with open(filepath, 'w') as f:
                                     f.write(content)
                                 print(f"Fixed {filepath}")
fix()
