all: ${PROJECT_ROOT}/artefacts/bin/wordvec1

${PROJECT_ROOT}/artefacts/bin/wordvec1: wordvec1.py
	python -m py_compile $<
	cp $< $@
	chmod +x $@

clean:
	rm -f ${PROJECT_ROOT}/artefacts/bin/wordvec1 *.pyc
