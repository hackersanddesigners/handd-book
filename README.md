H&D "BOOK" GENERATOR
====================

Scripts that generate a PDF fed from our wiki at: http://wiki.hackersanddesigners.nl

Requires python, pandoc, latex, etc.. Basically keep installing dependencies until it works. Ask Google if you have issues.

STEPS TO GENERATE PDF
---------------------

Step 1:
```
python get_wiki.py 
```

Missing python dependencies can be installed with:
```
pip install <module_name>
```

Step 2:
```
pandoc --template handd-book.template handd-book.wiki -o handd-book.pdf --toc -M fontsize=12pt -M author='Hackers \& Designers' -M title='About Bugs, Bots and Bytes' --latex-engine xelatex -M mainfont='Helvetica' -M papersize='a5paper' -V links-as-notes
```

Missing latex dependencies can be installed with:
```
tlmgr install <pkgname>
```

