all: ${PROJECT_ROOT}/artefacts/bin/selection

${PROJECT_ROOT}/artefacts/bin/selection: selection.py
	python -m py_compile $<
	cp $< $@
	chmod +x $@

clean:
	rm -f ${PROJECT_ROOT}/artefacts/bin/selection *.pyc
