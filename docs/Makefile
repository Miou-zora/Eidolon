WIN := Windows_NT

ifeq ($(OS),$(WIN))
  VENV_DIR = venv
  VENV_SCRIPT = ../$(VENV_DIR)/Scripts/
else
  VENV_SCRIPT =
endif

BUILD_DIR := .build

SPHINX_BUILD = $(VENV_SCRIPT)sphinx-build

.PHONY: all
all: html

.PHONY: html
html:
ifeq ($(OS),$(WIN))
	@ if not exist $(subst /,\,$@) mkdir $(subst /,\,$@)
else
	@ mkdir -p $(dir $@)
endif
	$(SPHINX_BUILD) . -b html $(BUILD_DIR)/html

.PHONY: clean
clean:
	$(RM) -rf $(BUILD_DIR)

.PHONY: re
re: clean
	$(MAKE) all
