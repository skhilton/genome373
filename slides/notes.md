to run the markdown to slides

pandoc -t revealjs -c skh.css -s -o myslides.html test.md -V revealjs-url=./reveal.js -i
pandoc week1.md --latex-engine=xelatex -o week1.pdf -V geometry:margin=1in --variable urlcolor=magenta
