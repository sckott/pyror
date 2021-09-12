import codecs
import re
from setuptools import setup
from setuptools import find_packages

version = ""
with open("pyror/__init__.py", "r") as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

if not version:
    raise RuntimeError("Cannot find version information")

with codecs.open("README.rst", "r", "utf-8") as f:
    readme = f.read()

long_description = "\n\n" + readme

setup(
    name="pyror",
    version=version,
    description="Research Organization Registry Python Client",
    long_description=long_description,
    author="Scott Chamberlain",
    author_email="myrmecocystus@gmail.com",
    url="https://github.com/sckott/pyror",
    license="MIT",
    packages=find_packages(
        exclude=[
            "test-*",
        ]
    ),
    install_requires=[
        "requests",
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "ror = pyror.scripts.rorid:ror",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
