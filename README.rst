sprockets.clients.cassandra
===========================
Provides base functionality for asynchronously accessing/modifying
data in a Cassandra cluster from within Tornado.

Althought the underlying library supports several connection options,
this module currently only allows the hostname to be specified, and 
that via an environment variable called CASSANDRA_URI as specified
in the docs.

|Version| |Downloads| |Status| |Coverage| |License|

Documentation
-------------
https://sprocketsclientcassandra.readthedocs.org

Contributing
------------
This project follows the standard fork and pull request model of development.
If you want to contribute changes, then fork the project and code
away. To set up the environment:

* virtualenv env
* source env/bin/activate
* pip install -qr dev-requirements.txt

To test across supported platforms:
* tox

To build the docs (in *build/sphinx/html*):
* ./setup.py build_sphinx

Version History
---------------
See https://github.com/sprockets/sprockets.clients.cassandra/blob/master/HISTORY.rst

.. |Version| image:: https://badge.fury.io/py/sprockets.clients.cassandra.svg?
   :target: https://badge.fury.io/py/sprockets.clients.cassandra

.. |Status| image:: https://travis-ci.org/sprockets/sprockets.clients.cassandra.svg?branch=master
   :target: https://travis-ci.org/sprockets/sprockets.clients.cassandra

.. |Coverage| image:: https://codecov.io/github/sprockets/sprockets.clients.cassandra/coverage.svg?branch=master
   :target: https://codecov.io/github/sprockets/sprockets.clients.cassandra?branch=master

.. |Downloads| image:: https://pypip.in/d/sprockets.clients.cassandra/badge.svg
   :target: https://pypi.python.org/pypi/sprockets.clients.cassandra

.. |License| iamge:: https://pypi.in/license/sprockets.clients.cassandra/badge.svg?
   :target: https://sprocketsclientscassandra.readthedocs.org
