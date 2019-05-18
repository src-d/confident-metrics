current_dir = $(shell pwd)

PROJECT = confident_metrics

DOCKERFILES = Dockerfile:$(PROJECT)
DOCKER_ORG = "srcd"

# Including ci Makefile
CI_REPOSITORY ?= https://github.com/src-d/ci.git
CI_BRANCH ?= v1
CI_PATH ?= .ci
MAKEFILE := $(CI_PATH)/Makefile.main
$(MAKEFILE):
	git clone --quiet --depth 1 -b $(CI_BRANCH) $(CI_REPOSITORY) $(CI_PATH);
-include $(MAKEFILE)

.PHONY: check
check:
	! (grep -R /tmp confident_metrics/tests)
	flake8 --count
	pylint confident_metrics

.PHONY: test
test:
	python3 -m unittest discover

