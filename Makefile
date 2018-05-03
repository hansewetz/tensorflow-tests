SUBDIRS = src 

include $(PROJECT_ROOT)/env/makerules/subdirs.rules

vcreate: vclean
	virtualenv venv
	(. venv/bin/activate&&pip install --upgrade jupyter matplotlib numpy pandas scipy scikit-learn tensorflow)

vclean:
	rm -rf venv

usage:
	@echo vcreate         - creates virtual environment
	@echo vclean          - removes virtual environment

