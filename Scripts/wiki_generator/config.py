COMMIT_HASH = "073b5fd"
TIMESTAMP = "2026-10-01T17:50:00Z"
GENERATED_BY = "agent:wiki-iso-documentation-standard"
VERIFIED = "true"

def make_frontmatter(doc_type, viewpoint, concept_type, title, description, tags, source_path=None):
    tags_str = ", ".join(f'"{t}"' for t in tags)
    source_line = f'source_path: "{source_path}"\n' if source_path else ""
    return f"""---
iso_doc_type: "{doc_type}"
iso_viewpoint: "{viewpoint}"
type: "{concept_type}"
title: "{title}"
{source_line}description: "{description}"
tags: [{tags_str}]
timestamp: "{TIMESTAMP}"
generated: "{GENERATED_BY}"
verified: "{VERIFIED}"
last_verified_commit: "{COMMIT_HASH}"
---"""
