all: build install

.PHONY: build install test docs distclean dist upload

install:
	pip install .

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

clean:
	rm -rf dist/* build/*

dist:
	python3 -m build --sdist --wheel

upload_test:
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload:
	python3 -m twine upload dist/*
