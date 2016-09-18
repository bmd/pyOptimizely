#!/usr/bin/env python

import os
import re
import sys
from codecs import open
from setuptools import setup
from pytest import *

packages = [
    'optimizely'
]

requires = [
    'requests>=2.0.0'
]

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
    url='http://github.com/bmd/pyOptimizely',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE'], 'requests': ['*.pem']},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    classifiers=(
        'Development Status :: 1 - In Development',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: MIT Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ),
    cmdclass={'test': PyTest},
    tests_require=test_requirements
)
