Files=Labors.pdf #Labors_def.pdf
Pandoc=pandoc

all: $(Files)

%_old.pdf: %.md
	$(Pandoc) $< -o $@ \
	--template=build/template \
	--latex-engine=xelatex

%_old.tex: %.md
	$(Pandoc) $< -o $@ \
	--template=build/template \
	--latex-engine=xelatex

%.pdf: %.md
	$(Pandoc) $< -o $@ \
	--latex-engine=xelatex \
	--variable=geometry:margin=0.5in \
	-H build_markdown/title.sty 
	
%.tex: %.md
	$(Pandoc) $< -o $@ \
	--latex-engine=xelatex \
	--variable=geometry:margin=0.5in \
	-H title.sty 
	
%.html: %.md
	$(Pandoc) $< -o $@ -m \
	-c http://johnmacfarlane.net/pandoc/demo/pandoc.css \
	-s -S --toc #Uztaisa satura rādītāju
	#-m #Math output
	
%_def.pdf: %.md
	$(Pandoc) $< -o $@ \
	--latex-engine=xelatex \
	-V header-includes:"\usepackage{csvsimple}" \
	-V geometry:margin=0.5in \
	#-V fontsize:12pt 
