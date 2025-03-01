from pathlib import Path
import subprocess
import re

repodir = Path(__file__).parent.parent.resolve()

def markdown_subst(written_files, regex, subst):
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
