#!/usr/bin/env python3

"""
A one-off script to replace some &nbsp; with normal spaces
"""
import argparse
from shared import markdown_subst

written_files = set()

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
        written_files,
        r"(\n#[^\n]*&nbsp;[^\n]*\n)",
        replacement_func,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--break-jekyll", required=True, choices=["yes", "no"])
    args = parser.parse_args()
    fix_nbsp(args.break_jekyll == "yes")
    print(f"Wrote to {len(written_files)} files.")
