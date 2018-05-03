all: ${PROJECT_ROOT}/artefacts/bin/tgrad

${PROJECT_ROOT}/artefacts/bin/tgrad: tgrad.py
	python -m py_compile $<
	cp $< $@
	chmod +x $@

clean:
	rm -f ${PROJECT_ROOT}/artefacts/bin/tgrad *.pyc
