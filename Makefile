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
	${VENV_SCRIPT}pyinstaller client/main.py --onefile

exe-server:
	${VENV_SCRIPT}pyinstaller server/main.py --onefile

.PHONY: client server exe-client exe-server