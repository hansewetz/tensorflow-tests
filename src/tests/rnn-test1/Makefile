all: ${PROJECT_ROOT}/artefacts/bin/rnn-test1

${PROJECT_ROOT}/artefacts/bin/rnn-test1: rnn-test1.py
	python -m py_compile $<
	cp $< $@
	chmod +x $@

clean:
	rm -f ${PROJECT_ROOT}/artefacts/bin/rnn-test1 *.pyc
