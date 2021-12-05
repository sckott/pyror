all: build install

.PHONY: build install test docs distclean dist upload

build:
	python3 setup.py build

install: build
	python3 setup.py install

test:
# 	pytest test/
	pytest --record-mode=once --cov-report term --cov=pyror test/
# 	pytest --record-mode=once test/

test_no_vcr:
	pytest --disable-recording --cov-report term --cov=pyror test/

docs:
	cd docs;\
	make html
	
opendocs:
	open docs/_build/html/index.html

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
