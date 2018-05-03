all: ${PROJECT_ROOT}/artefacts/bin/tmatmul

${PROJECT_ROOT}/artefacts/bin/tmatmul: tmatmul.py
	python -m py_compile $<
	cp $< $@
	chmod +x $@

clean:
	rm -f ${PROJECT_ROOT}/artefacts/bin/tmatmul *.pyc
