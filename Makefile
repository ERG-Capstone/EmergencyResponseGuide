# Make commands for building ERG source

all: build

build:
	python tools/build.py && \
	cp -r stage/* xdk/www/

install_deps:
	pip install -r requirements.txt
