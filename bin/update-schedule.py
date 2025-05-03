#!/usr/bin/env python3

from datetime import datetime
import os
import pathlib
import re
import sys


def select_year():
    """Select the year, cd into the corresponding directory, and return the year."""
    # Default to the current year:
    year = str(datetime.now().year)

    # Override based on the current directory:
    dirname = os.getcwd().split('/')[-1]
    if re.search("20[0-9]{2}", dirname):
        year = dirname

    # Override based on the CLI:
    if len(sys.argv) == 2:
        y = sys.argv[1]
        if re.search("20[0-9]{2}", y):
            year = y

    # cd into the correct directory:
    basedir = pathlib.Path(__file__).parent.parent.resolve()
    wd = basedir / "content" / year
    os.chdir(wd)

    return year

def main():
    year = select_year()
    # TODO: Rewrite:
    os.system(f"../../bin/convert_from_pretalx.py {year}")
    os.system(f"../../bin/json2md.py {year}")

if __name__ == "__main__":
    main()
