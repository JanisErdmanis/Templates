#LATEX=pdflatex
#LATEXMK=latexmk
LATEXOPT=-file-line-error


MAIN=mainfile
SOURCES=$(MAIN).tex Makefile #bib/plessl.bib
#FIGURES := $(shell ls fig/*.pdf)

all:    $(MAIN).pdf

.refresh:
	touch .refresh

$(MAIN).pdf: $(MAIN).tex .refresh $(SOURCES)
	latexmk -pdf -silent -xelatex -shell-escape -interaction=nonstopmode -synctex=1 $(MAIN).tex

force:
	touch .refresh
	$(MAKE) $(MAIN).pdf

.PHONY: clean force all


pythontex: 
	pythontex3 --rerun=always $(MAIN) #latexmk -pdf -silent -xelatex -shell-escape -interaction=nonstopmode -synctex=1 $(MAIN).tex


easy:
	make; make pythontex; make force


#mainfile.pdf: mainfile.tex
#    xelatex -synctex=1 --shell-escape -interaction=nonstopmode $^; pythontex3 $^; xelatex -synctex=1 --shell-escape -interaction=nonstopmode $^



clean:
	latex -C $(MAIN).tex
	rm -f $(MAIN).pdfsync
	rm -rf *~ *.tmp
