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

PROTO_FOLDER = ./proto

.PHONY: proto
proto:
	$(VENV_SCRIPT)pip install -e .

.PHONY: server
client: proto
	$(VENV_SCRIPT)python client/main.py

.PHONY: server
server: proto
	$(VENV_SCRIPT)python server/main.py

.PHONY: exe-client
exe-client: proto
	$(VENV_SCRIPT)pyinstaller --noconsole client/main.py --onefile --name=client

.PHONY: exe-server
exe-server: proto
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
