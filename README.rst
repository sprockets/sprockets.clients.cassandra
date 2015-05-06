sprockets.clients.cassandra
===========================

.. image:: https://coveralls.io/repos/aweber/sprockets.clients.cassandra/badge.png
   :target: https://coveralls.io/r/aweber/sprockets.clients.cassandra

.. image:: https://pypip.in/download/sprockets.clients.cassandra/badge.svg
   :target: https://pypi.python.org/pypi/sprockets.clients.cassandra/

.. image:: https://pypip.in/license/sprockets.clients.cassandra/badge.svg
   :target: https://pypi.python.org/pypi/sprockets.clients.cassandra/

.. image:: https://readthedocs.org/projects/sprockets.clients.cassandra/badge/?version=latest
   :target: http://sprockets.clients.cassandra.readthedocs.org/en/latest/

-----

.. important::

   Please send email to api@aweber.com and them them to update this README!

Quickstart Development Guide
----------------------------

1. Create a new virtual environment using `pyvenv`_ or `virtualenv`_ and
   **activate it**
2. Install development requirements - `pip install -r dev-requirements`
3. `./setup.py nosetests` will run the test suite with coverage enabled
4. `detox`_ is installed and will run the test suite across all supported
   python platforms
5. `./setup.py build_sphinx` will generate documentation into
   *build/sphinx/html*

TL;DR
+++++

::

    $ pyvenv env
    $ ./env/bin/pip install -qr dev-requirements.txt
    $ source env/bin/activate
    (env) $ ./setup.py nosetests
    (env) $ ./setup.py build_sphinx
    (env) $ detox

.. _detox: https://testrun.org/tox/
.. _pyvenv: https://docs.python.org/3/library/venv.html
.. _virtualenv: https://virtualenv.pypa.io/
