#!/usr/bin/env python3
"""Build index.html from resume.yaml + Jinja2 template."""

import json
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader
from jsonschema import validate, ValidationError

ROOT = Path(__file__).parent


def main():
    # Load data
    data = yaml.safe_load((ROOT / "resume.yaml").read_text())

    # Validate against schema
    schema = json.loads((ROOT / "resume.schema.json").read_text())
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        print(f"resume.yaml validation error: {e.message}", file=sys.stderr)
        print(f"  Path: {' → '.join(str(p) for p in e.absolute_path)}", file=sys.stderr)
        sys.exit(1)

    # Render template
    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        keep_trailing_newline=True,
        lstrip_blocks=True,
        trim_blocks=True,
    )
    template = env.get_template("base.html")
    html = template.render(**data)

    # Write output
    (ROOT / "index.html").write_text(html)
    print("Built index.html")


if __name__ == "__main__":
    main()
