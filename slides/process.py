"""
Process and populate weekly slide directories.

SKH 20190319
"""

import os
import subprocess
import glob

def make_md(title, nb, html, pdf, fname):
    # header = f"---\nlayout: page\ntitle:{title}\npermalink: /slides/week\n---\n"
    header = f"{title}\n"
    body = f"* [`jupyter notebook`]({nb})\n* [`html`]({html})\n* [`pdf`]({pdf})\n"
    with open(fname, "w") as f:
        f.write(header)
        f.write(body)
    print(f"Wrote to {fname}")


def main():
    clean = False
    for week_dir in glob.glob("week*/"):
        for nb in glob.glob(f"{week_dir}week*.ipynb"):
            # extract info from name
            prefix = os.path.splitext(os.path.basename(nb))[0]
            week = prefix.split("_")[1]
            date = prefix.split("_")[2]
            # define output names
            html_fname = f"{week_dir}{prefix}.slides.html"
            pdf_fname = f"{week_dir}{prefix}.pdf"
            md_fname = f"{week_dir}{prefix}.md"
            # define commands
            html_CMD = ["jupyter", "nbconvert", nb, "--to", "slides"]
            pdf_CMD = ["jupyter", "nbconvert", nb, "--to", "pdf"]
            if clean:
                subprocess.check_call(html_CMD)
                subprocess.check_call(pdf_CMD)
                make_md(f"week {week} ({date})", nb, html_fname, pdf_fname, md_fname)
            else:
                if not os.path.isfile(html_fname):
                    subprocess.check_call(html_CMD)
                else:
                    print(f"Already found file {html_fname}")
                if not os.path.isfile(pdf_fname):
                    subprocess.check_call(pdf_CMD)
                else:
                    print(f"Already found file {pdf_fname}")
                if not os.path.isfile(md_fname):
                    make_md(f"week {week} ({date})", nb, html_fname, pdf_fname, md_fname)
                else:
                    print(f"Already found file {md_fname}")



if __name__ == '__main__':
    main()
