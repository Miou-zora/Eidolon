ifeq ($(OS),Windows_NT)
PY 			=	py
else
PY			=	python
endif

ifeq ($(OS),Windows_NT)
VENV_DIR	=	venv
VENV_SCRIPT	=	${VENV_DIR}/Scripts/
VENV_PY		=	${VENV_DIR}/Lib/site-packages/
else
VENV_SCRIPT	=
endif

ifeq ($(OS),Windows_NT)
RM			=	del /s /q /f
RM_DIR		=	rd /s /q
else
RM			=	rm -f
RM_DIR		=	rm -rf
endif

ifeq ($(OS),Windows_NT)
FILE_SEP	=	\\
else
FILE_SEP	=	/
endif

PROTO_FOLDER	=	./proto

proto:
	${VENV_SCRIPT}python ${VENV_PY}grpc_tools${FILE_SEP}protoc.py -I. --python_out=. --pyi_out=. --grpc_python_out=. ${PROTO_FOLDER}/core.proto

client: proto
	${VENV_SCRIPT}pip install
	${VENV_SCRIPT}python client/main.py

server: proto
	${VENV_SCRIPT}python server/main.py

exe-client: proto
	${VENV_SCRIPT}pyinstaller --noconsole client${FILE_SEP}main.py --onefile --name=client

exe-server: proto
	${VENV_SCRIPT}pyinstaller server${FILE_SEP}main.py --onefile --name=server

clean:
	${RM} client.spec server.spec

ifeq ($(OS),Windows_NT)
	if exist build ${RM_DIR} build
else
	${RM_DIR} build
endif

fclean: clean
ifeq ($(OS),Windows_NT)
	if exist dist ${RM_DIR} dist
else
	${RM_DIR} dist
endif

.PHONY: client server exe-client exe-server proto