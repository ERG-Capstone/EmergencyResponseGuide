# Make commands for building ERG source

all: build

build:
	python tools/build.py

install_deps:
	pip install -r requirements.txt
