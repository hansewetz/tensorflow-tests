all: ${PROJECT_ROOT}/artefacts/bin/graph

${PROJECT_ROOT}/artefacts/bin/graph: graph.py
	python -m py_compile $<
	cp $< $@
	chmod +x $@

clean:
	rm -f ${PROJECT_ROOT}/artefacts/bin/graph *.pyc
