all: ${PROJECT_ROOT}/artefacts/bin/tplaceholder

${PROJECT_ROOT}/artefacts/bin/tplaceholder: tplaceholder.py
	python -m py_compile $<
	cp $< $@
	chmod +x $@

clean:
	rm -f ${PROJECT_ROOT}/artefacts/bin/tplaceholder *.pyc
