ifeq ($(OS),Windows_NT)
PY 		=	py
else
PY		=	python
endif

# TODO: add .exe packaging

all:
	${PY} main.py

mp:
	mypy