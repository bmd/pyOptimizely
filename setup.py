#!/usr/bin/env python

import os
import re
import sys

from codecs import open

from setuptools import setup
from setuptools.command.test import test as TestCommand

packages = [
    'requests',
    'requests.packages',
    'requests.packages.chardet',
    'requests.packages.urllib3',
    'requests.packages.urllib3.packages',
    'requests.packages.urllib3.contrib',
    'requests.packages.urllib3.util',
    'requests.packages.urllib3.packages.ssl_match_hostname',
]

requires = []

test_requirements = [
    'pytest>=2.8.0',
    'pytest-httpbin==0.0.7',
    'pytest-cov'
]

with open('requests/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='pyOptimizely',
    version=0.1,
    description='A minimal python wrapper for the Optimizely API',
    long_description=readme + '\n',
    author='Brendan Maione-Downing',
    author_email='b.maionedowning@gmail.com',
    url='http://python-requests.org',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE'], 'requests': ['*.pem']},
    package_dir={'requests': 'requests'},
    include_package_data=True,
    install_requires=requires,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 1 - In Development',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
        'Programming Language :: Python :: Implementation :: CPython',
    ),
    cmdclass={'test': PyTest},
    tests_require=test_requirements,
    extras_require={
        'security': [
            'pyOpenSSL>=0.13',
            'ndg-httpsclient',
            'pyasn1'
        ],
        'socks': [
            'PySocks>=1.5.6, !=1.5.7'
        ],
    },
)