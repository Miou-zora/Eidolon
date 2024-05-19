WIN := Windows_NT

ifeq ($(OS),$(WIN))
  PY = py
else
  PY = python
endif

ifeq ($(OS),$(WIN))
  VENV_DIR = venv
  VENV_SCRIPT = $(VENV_DIR)/Scripts/
  VENV_PY = $(VENV_DIR)/Lib/site-packages/
else
  VENV_SCRIPT =
endif

ifeq ($(OS),Windows_NT)
  RM = del /s /q /f
  RM_DIR = rd /s /q
else
  RM_DIR = rm -rf
endif

ifeq ($(OS),$(WIN))
  TOUCH = type nul >
else
  TOUCH = touch
endif

PROTO_FOLDER = ./proto

COMMON_INSTALL_FILE = .install

.PHONY: common
common: $(COMMON_INSTALL_FILE)

$(COMMON_INSTALL_FILE):
	$(TOUCH) $(COMMON_INSTALL_FILE)
	$(VENV_SCRIPT)pip install -e .

.PHONY: server
client: common
	$(VENV_SCRIPT)python client/main.py

.PHONY: server
server: common
	$(VENV_SCRIPT)python server/main.py

.PHONY: exe-client
exe-client: common
	$(VENV_SCRIPT)pyinstaller --noconsole client/main.py --onefile --name=client

.PHONY: exe-server
exe-server: common
	$(VENV_SCRIPT)pyinstaller server/main.py --onefile --name=server

.PHONY: clean
clean:
	$(RM) client.spec server.spec

ifeq ($(OS),$(WIN))
	if exist build $(RM_DIR) build
else
	$(RM_DIR) build
endif

.PHONY: fclean
fclean: clean
ifeq ($(OS),$(WIN))
	if exist dist ${RM_DIR} dist
else
	$(RM_DIR) dist
endif
