## Making changes

Most files can be edited directly. If you're making changes to the schedule,
please go inside the directory for the current year, manually edit `talks.json`
and run `../../bin/update.sh` to update the schedule on the Website (Markdown
files in `talks/`) and Giggity (XML file `giggity.xml`).
Please include all relevant changes (at least three files) in your commit.
If you don't want to run the scripts you may also only change `talks.json` or
open an issue.

You can either open a pull request on GitHub or send patches (`git-send-email`)
to `info@tuebix.org`.

## How to build

Run
```
hugo server
```
in the root-directory of this repository and point your browser
toward the link shown in stdout. It will auto-update if you change
the source files of hugo (e.g. the Markdown files).

## This site is live on [tuebix.org](https://www.tuebix.org)

See `.github/workflows/hugo.yaml` for information how this works.

Anything commited to the `main` branch will be go live
a few minutes after it is pushed.
