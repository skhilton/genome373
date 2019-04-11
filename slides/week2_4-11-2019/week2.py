# Examples from quiz section #2
# SKH 20190410

# Variables and types
x = 5
print(type(x))


'pandoc' 'week2.md' '--latex-engine=xelatex' '-o', 'week2.pdf' '-V', 'geometry:margin=1in' '--variable'urlcolor=magenta'
pandoc week2.md --latex-engine==xelatex -o week2.pdf -V geometry:margin=1in --variable urlcolor=magenta