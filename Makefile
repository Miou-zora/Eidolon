ifeq ($(OS),Windows_NT)
PY 		=	py
else
PY		=	python
endif

all:
	${PY} main.py