#!/usr/bin/env python
import codecs
import sys

from setuptools import setup, find_packages

import sprockets.clients.cassandra


def read_requirements_file(filename):
    """Read pip-formatted requirements from a file."""
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()
                if not line.startswith('#')]

requirements = read_requirements_file('requirements.txt')
test_requirements = read_requirements_file('test-requirements.txt')

setup(
    name='sprockets.clients.cassandra',
    description='Base functioanlity for accessing/modifying data in Cassandra',
    version=sprockets.clients.cassandra.__version__,
    packages=find_packages(exclude=['tests', 'tests.*']),
    test_suite='nose.collector',
    include_package_data=True,
    long_description=codecs.open('README.rst', encoding='utf-8').read(),
    install_requires=requirements,
    tests_require=test_requirements,
    author='AWeber Communications, Inc.',
    author_email='api@aweber.com',
    url='https://github.com/aweber/sprockets.clients.cassandra',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
