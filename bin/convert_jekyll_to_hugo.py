#!/usr/bin/env python3

"""
A one-off script used for preparing to transition from jekyll to hugo
"""
from shared import markdown_subst
import re

written_files = set()


def permalink_to_url():
    """
    Replace every `permalink: ...` in the frontmatter of markdown files with `permalink: ... \n url: ...`

    This function is idempotent
    """

    def replacement_func(matchobj):
        assert "url" not in matchobj.group(0)
        return matchobj.group(1) + "url:" + matchobj.group(3) + matchobj.group(4)

    markdown_subst(
        written_files,
        "^(---((?!---).)*)permalink:([^\n]*)(\n((?!url)(?!---).)*---)", replacement_func
    )


def add_needed_heading_ids():
    def replacement_func(matchobj):
        if "{#" in matchobj.group(0):
            return matchobj.group(0)
        id = (
            matchobj.group(1)
            .rstrip()
            .replace(":", "")
            .replace("(", "")
            .replace(")", "")
            .replace(" ", "-")
            .lower()
        )
        return matchobj.group(0).rstrip() + f" {{#{id}}}\n"

    markdown_subst(
        written_files,
        re.escape('### <img height = "32" src="../../..')
        + '/images/[a-z0-9]*\\.svg">'
        + r"([^\n]*)\n",
        replacement_func,
    )


if __name__ == "__main__":
    permalink_to_url()
    add_needed_heading_ids()
    print(f"Wrote to {len(written_files)} files.")
