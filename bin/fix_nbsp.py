#!/usr/bin/env python3

"""
A one-off script to replace some &nbsp; with normal spaces
"""

from pathlib import Path
import subprocess
import re
import argparse

repodir = Path(__file__).parent.parent.resolve()

written_files = set()


def markdown_subst(regex, subst):
    """
    Replaces `regex` with `subst` in every Markdown file in the repository
    """

    for fp in repodir.rglob("**/*.md"):
        returncode = subprocess.run(
            ["git", "check-ignore", "--", fp], stdout=subprocess.DEVNULL
        ).returncode
        assert returncode in [0, 1]
        if not returncode:
            continue
        old_content = fp.read_text()
        new_content = re.sub(
            regex,
            subst,
            old_content,
            flags=re.DOTALL,
        )
        if new_content != old_content:
            written_files.add(fp)
            Path(fp).write_text(new_content)


def fix_nbsp(break_jekyll: bool):
    def replacement_func(matchobj):
        if "{#" in matchobj.group(0):
            return matchobj.group(0)
        ignored_for_id = [
            "&nbsp;",
            "&",
            "–",
            "+",
            ",",
            ".",
            ":",
            '"',
            "’",
            "?",
            "/",
        ]
        id = matchobj.group(0).strip()
        while id[0] == "#":
            id = id[1:]
        for ignored in ignored_for_id:
            id = id.replace(ignored, "")
        id = id.strip().replace(" ", "-").lower()

        if (
            not break_jekyll and id[0].isdigit()
        ):  # Jekyll/Kramdown does not parse something like {#3abc} as an id
            return matchobj.group(0)

        return matchobj.group(0).replace("&nbsp;", " ").rstrip() + f" {{#{id}}}\n"

    markdown_subst(
        r"(\n#[^\n]*&nbsp;[^\n]*\n)",
        replacement_func,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--break-jekyll", required=True, choices=["yes", "no"])
    args = parser.parse_args()
    fix_nbsp(args.break_jekyll == "yes")
    print(f"Wrote to {len(written_files)} files.")
