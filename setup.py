#!/usr/bin/env python

from codecs import open
from setuptools import setup

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
    packages=['optimizely'],
    package_data={'': ['LICENSE', 'NOTICE'], 'requests': ['*.pem']},
    include_package_data=True,
    install_requires=[
        'requests>=2.0.0'
    ],
    license='MIT',
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ),
    tests_require=[
        'pytest>=2.8.0',
        'pytest-httpbin==0.0.7',
        'pytest-cov'
    ]
)
