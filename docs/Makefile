BUILD_DIR := .build

SPHINX_BUILD = sphinx-build

.PHONY: all
all: html

.PHONY: html

html:
	@ mkdir -p $(dir $@)
	$(SPHINX_BUILD) . -b html $(BUILD_DIR)/html

.PHONY: clean
clean:
	$(RM) -rf $(BUILD_DIR)

.PHONY: re
re: clean
	$(MAKE) all
