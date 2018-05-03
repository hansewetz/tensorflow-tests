all: ${PROJECT_ROOT}/artefacts/bin/tvars

${PROJECT_ROOT}/artefacts/bin/tvars: tvars.py
	python -m py_compile $<
	cp $< $@
	chmod +x $@

clean:
	rm -f ${PROJECT_ROOT}/artefacts/bin/tvars
