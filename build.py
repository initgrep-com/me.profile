#!/usr/bin/env python3
"""Build index.html from data.yaml + Jinja2 template."""

import json
import sys
from datetime import datetime
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader
from jsonschema import validate, ValidationError

ROOT = Path(__file__).parent


def format_date(value):
    """Format ISO date (2025-01) as display date (Jan 2025). Passes through 'present' and integers."""
    if value == "present":
        return "Present"
    s = str(value)
    if s.isdigit():
        return s
    return datetime.strptime(s, "%Y-%m").strftime("%b %Y")


def main():
    # Load data
    data = yaml.safe_load((ROOT / "data.yaml").read_text())

    # Validate against schema
    schema = json.loads((ROOT / "resume.schema.json").read_text())
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        print(f"data.yaml validation error: {e.message}", file=sys.stderr)
        print(f"  Path: {' → '.join(str(p) for p in e.absolute_path)}", file=sys.stderr)
        sys.exit(1)

    # Render template
    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        keep_trailing_newline=True,
        lstrip_blocks=True,
        trim_blocks=True,
    )
    env.filters["format_date"] = format_date
    template = env.get_template("base.html")
    html = template.render(**data)

    # Write output
    (ROOT / "index.html").write_text(html)
    print("Built index.html")


if __name__ == "__main__":
    main()
