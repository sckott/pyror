all: build install

.PHONY: build install test docs distclean dist upload

build:
	python3 setup.py build

install: build
	python3 setup.py install

test:
	pytest test/
# 	pytest --disable-vcr --cov-report term --cov=pyror test/

docs:
	cd docs;\
	make html
	# open _build/html/index.html

distclean:
	rm dist/*

dist:
	python3 setup.py sdist
	python3 setup.py bdist_wheel --universal

register:
	python3 setup.py register

upload_test:
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload:
	python3 -m twine upload dist/*
