ifeq ($(OS),Windows_NT)
PY 		=	py
else
PY		=	python
endif

ifeq ($(OS),Windows_NT)
VENV_DIR	=	venv
endif


all:
	${PY} main.py

exe:
ifeq ($(OS),Windows_NT)
	${VENV_DIR}/Scripts/pyinstaller main.py --onefile
else
	pyinstaller main.py --onefile
endif

