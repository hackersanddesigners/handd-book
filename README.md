Method 1
========

Step 1:
```
python get_wiki.py 
```

Step 2:
```
pandoc --template article.template  test.wiki -o article.pdf --toc -M fontsize=12pt -M title='Hackers \& Designers' -M subtitle='About Bugs, Bots and Bytes' --latex-engine xelatex -M mainfont='Helvetica'
```
