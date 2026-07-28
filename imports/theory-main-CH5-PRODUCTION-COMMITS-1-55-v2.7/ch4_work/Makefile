MAIN=main
LATEXMK=latexmk

.PHONY: all pdf check clean distclean state

all: pdf

pdf:
	$(LATEXMK) -pdf $(MAIN).tex

check: pdf
	@test -f build/$(MAIN).pdf
	@! grep -E "LaTeX Warning: (Reference|Citation).*undefined|There were undefined references" build/$(MAIN).log
	@echo "PR-BOOK-15.2 Phase V checks passed."

clean:
	$(LATEXMK) -c $(MAIN).tex

# Remove all reproducible build output.
distclean:
	$(LATEXMK) -C $(MAIN).tex
	rm -rf build build_*

state:
	python3 tools/book_state.py
