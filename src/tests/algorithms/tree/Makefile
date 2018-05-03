all: ${PROJECT_ROOT}/artefacts/bin/tree

${PROJECT_ROOT}/artefacts/bin/tree: tree.py
	python -m py_compile $<
	cp $< $@
	chmod +x $@

clean:
	rm -f ${PROJECT_ROOT}/artefacts/bin/tree *.pyc
