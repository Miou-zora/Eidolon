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



all:
	${VENV_SCRIPT}python main.py

exe:
	${VENV_SCRIPT}pyinstaller main.py --onefile

