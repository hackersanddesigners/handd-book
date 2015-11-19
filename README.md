H&D "BOOK" GENERATOR
====================

Scripts that generate a PDF fed from our wiki at: http://wiki.hackersanddesigners.nl

Requires python, pandoc, latex, etc., basically keep install dependencies until it works. Ask Google if you have issues.

STEPS TO GENERATE PDF
---------------------

Step 1:
```
python get_wiki.py 
```

Step 2:
```
pandoc --template article.template  test.wiki -o article.pdf --toc -M fontsize=12pt -M title='Hackers \& Designers' -M subtitle='About Bugs, Bots and Bytes' --latex-engine xelatex -M mainfont='Helvetica' -M papersize='a4paper'
```
