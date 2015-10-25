all: clean tex pdf

pdf: 
	pdflatex handd_book.tex
	pdflatex handd_book.tex
	pdflatex handd_book.tex

tex:
	python make_book.py

clean:
	-rm *.log *.aux *.out *.pdf *.toc handd_book.tex

clean-images:
	-rm *.jpg *.JPG *.png *.PNG

