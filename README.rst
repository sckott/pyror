pyror
========

|docs| |ghactions| |black|

A client for ROR's API

`ROR API docs <https://ror.readme.io/docs/rest-api>`__

Installation
============

Dev version

.. code-block:: console

    pip (or pip3) install git+git://github.com/sckott/pyror.git#egg=pyror

    # OR

    git clone git@github.com:sckott/pyror.git
    cd pyror
    make install

Usage
=====

Initialize a client

.. code-block:: python

    from pyror import ror_id
    ror_id('026tem613')

Meta
====

* Please note that this project is released with a `Contributor Code of Conduct <https://github.com/sckott/pyror/blob/master/CODE_OF_CONDUCT.md>`__. By participating in this project you agree to abide by its terms.
* License: MIT; see `LICENSE file <https://github.com/sckott/pyror/blob/master/LICENSE>`__

.. |docs| image:: https://readthedocs.org/projects/pyror/badge/?version=latest
   :target: http://pyror.rtfd.org/

.. |ghactions| image:: https://github.com/sckott/pyror/workflows/Python/badge.svg
   :target: https://github.com/sckott/pyror/actions?query=workflow%3APython

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

