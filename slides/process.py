"""
Process and populate weekly slide directories.

SKH 20190319
"""

import os
import subprocess
import glob


def make_md(title, html, pdf, fname):
    header = f"---\nlayout: page\ntitle: {title}\n---\n"
    body = f"* [`html`]({os.path.basename(html)})\n* [`pdf`]({os.path.basename(pdf)})\n"
    with open(fname, "w") as f:
        f.write(header)
        f.write(body)
    print(f"Wrote to {fname}")


def main():
    clean = True
    for week_dir in glob.glob("week*/"):
        print(week_dir)
        os.chdir(week_dir)
        print(os.getcwd())
        week = os.path.dirname(week_dir).split("_")[0][4:]
        date = os.path.dirname(week_dir).split("_")[1]
        md_fname = f"week{week}.md"
        print(md_fname)
        assert os.path.isfile(md_fname)
        # define output names
        html_fname = f"week{week}.html"
        pdf_fname = f"week{week}.pdf"
        toc_fname = f"week{week}_toc.md"
        title = f"week {week} ({date})"
        print(title)
        # define commands
        html_CMD = ["pandoc", "-t", "revealjs", "-c", "../skh.css", "-o",
                    html_fname, md_fname, "-V", "revealjs-url=../reveal.js", "-i"]
        pdf_CMD = ["pandoc", md_fname, "--latex-engine=xelatex", "-o",
                   pdf_fname, "-V", "geometry:margin=1in", "--variable",
                   "urlcolor=magenta"]
        if clean:
            subprocess.check_call(html_CMD)
            subprocess.check_call(pdf_CMD)
            make_md(title, html_fname, pdf_fname, toc_fname)
        else:
            if not os.path.isfile(html_fname):
                subprocess.check_call(html_CMD)
            else:
                print(f"Already found file {html_fname}")
            if not os.path.isfile(pdf_fname):
                subprocess.check_call(pdf_CMD)
            else:
                print(f"Already found file {pdf_fname}")
        os.chdir("../")
        print(os.getcwd())
        print("done")

if __name__ == '__main__':
    main()
