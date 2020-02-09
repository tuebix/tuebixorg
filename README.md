## Making changes

Most files can be edited directly. If you're making changes to the schedule,
please go inside the directory for the current year, manually edit `talks.json`
and run `../bin/update.sh` to update the schedule on the Website (Markdown files
in `talks/`) and Giggity (XML file `giggity.xml`).
Please include all relevant changes (at least three files) in your commit.
If you don't want to run the scripts you may also only change `talks.json` or
open an issue.

You can either open a pull request on GitHub or send patches (`git-send-email`)
to `info@tuebix.org`.

## Jekyll

### get jekyll running 

in order to contribute you'll need ruby and 'jekyll' installed:
follow this guide:
https://jekyllrb.com/
as soon as 'jekyll serve' works, you should be fine

### clone tuebixorg

now it's time to clone:
git clone https://github.com/tuebix/tuebixorg.git

### try jekyll with tuebixorg

just mess around and watch the local changes with "jekyll serve"
have fun!

https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

### jekyll with github-pages

connection with github was set up along this guide:
https://24ways.org/2013/get-started-with-github-pages/
