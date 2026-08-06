#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = ROOT / "products"
REQUIRED_DIRS = ("research", "ux", "decisions", "stories", "evaluations")
REQUIRED_FIELDS = ("product", "artifact_type", "run_id", "date", "status", "sources")
errors = []
run_ids = {}

for product_dir in sorted(path for path in PRODUCTS.iterdir() if path.is_dir()):
    for directory in REQUIRED_DIRS:
        if not (product_dir / directory).is_dir():
            errors.append(f"missing directory: {product_dir.name}/{directory}")
    for document in sorted(product_dir.rglob("*.md")):
        text = document.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            errors.append(f"missing front matter: {document.relative_to(ROOT)}")
            continue
        front_matter = text.split("---\n", 2)[1]
        values = {}
        for line in front_matter.splitlines():
            match = re.match(r"^([a-z_]+):\s*(.*)$", line)
            if match:
                values[match.group(1)] = match.group(2).strip()
        for field in REQUIRED_FIELDS:
            if field not in values:
                errors.append(f"missing {field}: {document.relative_to(ROOT)}")
        if values.get("product") != product_dir.name:
            errors.append(f"product mismatch: {document.relative_to(ROOT)}")
        run_id = values.get("run_id")
        if run_id:
            if run_id in run_ids:
                errors.append(f"duplicate run_id {run_id}: {document.relative_to(ROOT)} and {run_ids[run_id]}")
            run_ids[run_id] = document.relative_to(ROOT)
        for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
            if not target.startswith(("http://", "https://", "#")) and not (document.parent / target).resolve().exists():
                errors.append(f"broken link {target}: {document.relative_to(ROOT)}")

if errors:
    print("Workspace validation failed:\n- " + "\n- ".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"Workspace validation passed: {len(run_ids)} unique artifacts")
