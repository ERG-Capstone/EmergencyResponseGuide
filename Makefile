# Make commands for building ERG source

all: build

build:
	# Line to assemble html resources goes here
	python tools/build.py

install_deps:
	pip install -r requirements.txt
	
