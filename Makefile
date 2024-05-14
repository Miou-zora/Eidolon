ifeq ($(OS),Windows_NT)
PY 		=	py
else
PY		=	python
endif

ifeq ($(OS),Windows_NT)
VENV_DIR	=	venv
VENV_SCRIPT	=	${VENV_DIR}/Scripts/
else
VENV_SCRIPT	=
endif


client:
	${VENV_SCRIPT}python client/main.py

server:
	${VENV_SCRIPT}python server/main.py

exe-client:
	${VENV_SCRIPT}pyinstaller --noconsole client/main.py --onefile --name=client

exe-server:
	${VENV_SCRIPT}pyinstaller server/main.py --onefile --name=server

clean:


.PHONY: client server exe-client exe-server