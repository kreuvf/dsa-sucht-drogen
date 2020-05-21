DSASUCHTDROGEN = \
	preamble.tex \
	title.tex \
	abstract.tex \
	nomencl-entries.tex \
	indices.tex \
	preface.tex \
	sucht-original.tex \
	sucht-hausregel.tex \
	random-drugs.tex \
	tail.tex
FIGS = \
	Regelübersicht_600dpi.png

dsa-sucht-drogen.pdf: figs _dsa-sucht-drogen.tex dsa-refs.bib
	xelatex _dsa-sucht-drogen.tex
	makeindex _dsa-sucht-drogen.nlo -s nomencl.ist -o _dsa-sucht-drogen.nls
	biber _dsa-sucht-drogen
	mv _dsa-sucht-drogen.pdf dsa-sucht-drogen.pdf

_dsa-sucht-drogen.tex: $(DSASUCHTDROGEN)
	cat $(DSASUCHTDROGEN) > ./$@

once: _dsa-sucht-drogen.tex
	mv _dsa-sucht-drogen.pdf dsa-sucht-drogen.pdf

thrice: _dsa-sucht-drogen.tex
	xelatex _dsa-sucht-drogen.tex
	makeindex _dsa-sucht-drogen.nlo -s nomencl.ist -o _dsa-sucht-drogen.nls
	biber _dsa-sucht-drogen
	xelatex _dsa-sucht-drogen.tex
	biber _dsa-sucht-drogen
	mv _dsa-sucht-drogen.pdf dsa-sucht-drogen.pdf

xfour: _dsa-sucht-drogen.tex
	xelatex _dsa-sucht-drogen.tex
	makeindex _dsa-sucht-drogen.nlo -s nomencl.ist -o _dsa-sucht-drogen.nls
	biber _dsa-sucht-drogen
	xelatex _dsa-sucht-drogen.tex
	biber _dsa-sucht-drogen
	xelatex _dsa-sucht-drogen.tex
	biber _dsa-sucht-drogen
	mv _dsa-sucht-drogen.pdf dsa-sucht-drogen.pdf

figs: $(FIGS)

%_600dpi.png: %.svg
	inkscape -z -d 600 -b white -e $@ $^
	optipng $@

clean-tex:
	rm -f _dsa-sucht-drogen.tex
	rm -f _dsa-sucht-drogen.bbl \
	_dsa-sucht-drogen.bcf \
	_dsa-sucht-drogen.blg \
	_dsa-sucht-drogen.ilg \
	_dsa-sucht-drogen.lof \
	_dsa-sucht-drogen.log \
	_dsa-sucht-drogen.lol \
	_dsa-sucht-drogen.lot \
	_dsa-sucht-drogen.lox \
	_dsa-sucht-drogen.mw \
	_dsa-sucht-drogen.nlo \
	_dsa-sucht-drogen.nls \
	_dsa-sucht-drogen.out \
	_dsa-sucht-drogen.run.xml \
	_dsa-sucht-drogen.toc

clean-intermediary:
	rm -f pythontex-files-_dsa-sucht-drogen/pythontex_data.pkl \
	pythontex-files-_dsa-sucht-drogen/_dsa-sucht-drogen.pytxmcr \
	pythontex-files-_dsa-sucht-drogen/*.stdout \
	pythontex-files-_dsa-sucht-drogen/_dsa-sucht-drogen.pytxpyg \
	_dsa-sucht-drogen.pytxcode \
	_dsa-sucht-drogen.aux	
	if [ -d pythontex-files-_dsa-sucht-drogen ] ; then rmdir pythontex-files-_dsa-sucht-drogen ; fi

clean-figs:
	rm -f $(FIGS)

clean-almost-all: clean-intermediary clean-figs clean-tex

clean-all: clean-almost-all
	rm -f dsa-sucht-drogen.pdf

.PHONY: once thrice xfour \
	clean-tex \
	clean-intermediary clean-figs clean-almost-all clean-all
