python-rrdtool package
======================

This is a working Python Package of RRDtool binding to Python.
It delivers the same API as original binding (actually, it IS original
binding, but installable via pip.)

Useful links:

- RRDTool webpage: http://oss.oetiker.ch/rrdtool/
- RRDTool Python module: http://oss.oetiker.ch/rrdtool/prog/rrdpython.en.html

Installation
------------

A few development (header) files are required to build ``python-rrdtool``: for
Python, libcairo2, libpango, libxml2, libglib2 and librrd. In Ubuntu run:
``sudo apt-get install libcairo2-dev libpango1.0-dev libglib2.0-dev libxml2-dev librrd-dev``

In virtualenv: ``pip install python-rrdtool``

From archive: ``pip install python-rrdtool-1.4.7.tar.gz``

From sources: ``python setup.py install``
