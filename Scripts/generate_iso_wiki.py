#!/usr/bin/env python3
"""
generate_iso_wiki.py

Primary orchestrator generating the complete ISO/IEC/IEEE 42010:2022 and 15289:2019
compliant wiki documentation in wiki/ adhering strictly to the wiki-iso-documentation-standard skill.
"""

import os
import sys
import shutil
import glob
import re

# Ensure Scripts/ is in sys.path
sys.path.insert(0, os.path.dirname(__file__))

from wiki_generator.root_pages import (
    get_home_md,
    get_readme_md,
    get_sidebar_md,
    get_index_md,
    get_glossary_md,
)
from wiki_generator.architecture_pages import (
    get_business_context_md,
    get_strategic_design_md,
    get_tactical_design_md,
    get_agent_specifications_md,
    get_runtime_sequences_md,
    get_infrastructure_adapters_md,
    get_mission_data_model_md,
)
from wiki_generator.security_pages import (
    get_security_architecture_md,
    get_hitl_governance_md,
    get_verification_triad_md,
    get_compliance_audit_md,
)
from wiki_generator.operations_pages import (
    get_user_manual_md,
    get_production_operations_md,
    get_experiment_logs_md,
)
from wiki_generator.quality_pages import (
    get_test_plan_report_md,
)
from wiki_generator.module_pages import (
    get_module_pages,
)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WIKI_DIR = os.path.join(BASE_DIR, "wiki")

def clean_wiki():
    if os.path.exists(WIKI_DIR):
        for item in os.listdir(WIKI_DIR):
            if item == ".git":
                continue
            item_path = os.path.join(WIKI_DIR, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
    os.makedirs(os.path.join(WIKI_DIR, "architecture"), exist_ok=True)
    os.makedirs(os.path.join(WIKI_DIR, "security"), exist_ok=True)
    os.makedirs(os.path.join(WIKI_DIR, "operations"), exist_ok=True)
    os.makedirs(os.path.join(WIKI_DIR, "quality"), exist_ok=True)
    os.makedirs(os.path.join(WIKI_DIR, "modules", "regression_model_template", "controller"), exist_ok=True)
    os.makedirs(os.path.join(WIKI_DIR, "modules", "regression_model_template", "core"), exist_ok=True)
    os.makedirs(os.path.join(WIKI_DIR, "modules", "regression_model_template", "io"), exist_ok=True)
    os.makedirs(os.path.join(WIKI_DIR, "modules", "regression_model_template", "jobs"), exist_ok=True)
    os.makedirs(os.path.join(WIKI_DIR, "modules", "regression_model_template", "utils"), exist_ok=True)

def write_page(rel_path, content):
    full_path = os.path.join(WIKI_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated: wiki/{rel_path}")

def generate_all():
    print("Step 1: Cleaning and preparing directory taxonomy...")
    clean_wiki()

    print("Step 2: Generating Root Navigation & Index pages...")
    write_page("Home.md", get_home_md())
    write_page("README.md", get_readme_md())
    write_page("_Sidebar.md", get_sidebar_md())
    write_page("index.md", get_index_md())
    write_page("GLOSSARY.md", get_glossary_md())

    print("Step 3: Generating Architecture Viewpoint pages (ISO 42010)...")
    write_page("architecture/business_context.md", get_business_context_md())
    write_page("architecture/strategic_design.md", get_strategic_design_md())
    write_page("architecture/tactical_design.md", get_tactical_design_md())
    write_page("architecture/agent_specifications.md", get_agent_specifications_md())
    write_page("architecture/runtime_sequences.md", get_runtime_sequences_md())
    write_page("architecture/infrastructure_adapters.md", get_infrastructure_adapters_md())
    write_page("architecture/mission_data_model.md", get_mission_data_model_md())

    print("Step 4: Generating Security & Governance pages...")
    write_page("security/security_architecture.md", get_security_architecture_md())
    write_page("security/hitl_governance.md", get_hitl_governance_md())
    write_page("security/verification_triad.md", get_verification_triad_md())
    write_page("security/compliance_audit.md", get_compliance_audit_md())

    print("Step 5: Generating Operations & Runbook pages...")
    write_page("operations/user_manual.md", get_user_manual_md())
    write_page("operations/production_operations.md", get_production_operations_md())
    write_page("operations/experiment_logs.md", get_experiment_logs_md())

    print("Step 6: Generating Quality & Test Plan pages (ISO 25010)...")
    write_page("quality/test_plan_report.md", get_test_plan_report_md())

    print("Step 7: Generating 1:1 Codebase Mirror Module pages (29 files)...")
    module_pages = get_module_pages()
    for rel_path, content in module_pages.items():
        write_page(rel_path, content)

    print(f"Total documents generated: {5 + 7 + 4 + 3 + 1 + len(module_pages)}")

def verify_links():
    print("\n--- Verifying Relative Link Integrity ---")
    files = glob.glob(os.path.join(WIKI_DIR, "**/*.md"), recursive=True)
    link_regex = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    broken = []
    total_links = 0
    for fpath in files:
        source_dir = os.path.dirname(fpath)
        with open(fpath, "r", encoding="utf-8") as fp:
            for idx, line in enumerate(fp, 1):
                for m in link_regex.finditer(line):
                    target = m.group(2).split("#")[0]
                    if not target or target.startswith(("http:", "https:", "mailto:")):
                        continue
                    total_links += 1
                    cand = [
                        os.path.normpath(os.path.join(source_dir, target)),
                        os.path.normpath(os.path.join(source_dir, target + ".md")),
                    ]
                    if not any(os.path.exists(c) for c in cand):
                        rel_source = os.path.relpath(fpath, BASE_DIR)
                        broken.append((rel_source, idx, m.group(1), target))

    print(f"Total internal links checked: {total_links}")
    if broken:
        print(f"ERROR: Found {len(broken)} broken links:")
        for b in broken:
            print(f"  {b[0]}:{b[1]} -> [{b[2]}]({b[3]})")
        return False
    print("SUCCESS: 0 broken links found! All relative cross-references resolve.")
    return True

def verify_source_coverage():
    print("\n--- Verifying 1:1 Source Coverage ---")
    src_files = glob.glob(os.path.join(BASE_DIR, "src", "regression_model_template", "**", "*.py"), recursive=True)
    missing = []
    for sf in src_files:
        rel = os.path.relpath(sf, os.path.join(BASE_DIR, "src"))
        doc_rel = os.path.splitext(rel)[0] + ".md"
        expected_md = os.path.join(WIKI_DIR, "modules", doc_rel)
        if not os.path.exists(expected_md):
            missing.append((rel, expected_md))

    print(f"Total Python source files checked: {len(src_files)}")
    if missing:
        print(f"ERROR: {len(missing)} source files missing corresponding wiki module docs:")
        for m in missing:
            print(f"  Source: {m[0]} -> Expected: {m[1]}")
        return False
    print("SUCCESS: 100% 1:1 Source coverage achieved! All 29 Python modules have dedicated wiki pages.")
    return True

def verify_frontmatter():
    print("\n--- Verifying Frontmatter Compliance ---")
    files = glob.glob(os.path.join(WIKI_DIR, "**/*.md"), recursive=True)
    invalid = []
    for fpath in files:
        if os.path.basename(fpath) == "_Sidebar.md":
            continue
        with open(fpath, "r", encoding="utf-8") as fp:
            content = fp.read()
        rel_fpath = os.path.relpath(fpath, BASE_DIR)
        if not content.startswith("---"):
            invalid.append((rel_fpath, "Missing opening frontmatter delimiter"))
            continue
        if "iso_doc_type:" not in content or "iso_viewpoint:" not in content:
            invalid.append((rel_fpath, "Missing iso_doc_type or iso_viewpoint"))
            continue

    if invalid:
        print(f"ERROR: Found {len(invalid)} non-compliant frontmatter files:")
        for inv in invalid:
            print(f"  {inv[0]}: {inv[1]}")
        return False
    print(f"SUCCESS: All {len(files) - 1} content documents comply with ISO 42010/15289 frontmatter!")
    return True

if __name__ == "__main__":
    generate_all()
    links_ok = verify_links()
    cov_ok = verify_source_coverage()
    fm_ok = verify_frontmatter()

    if links_ok and cov_ok and fm_ok:
        print("\n🏆 ISO WIKI GENERATION & VERIFICATION COMPLETE: ALL GATES PASS GREEN.")
        sys.exit(0)
    else:
        print("\n❌ VERIFICATION FAILED.")
        sys.exit(1)
