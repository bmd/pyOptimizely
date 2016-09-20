pyOptimizely
============

[![Build Status](https://travis-ci.org/bmd/pyOptimizely.svg?branch=master)](https://travis-ci.org/bmd/pyOptimizely)
[![Coverage Status](https://coveralls.io/repos/github/bmd/pyOptimizely/badge.svg?branch=master)](https://coveralls.io/github/bmd/pyOptimizely?branch=master)
[![Code Health](https://landscape.io/github/bmd/pyOptimizely/master/landscape.svg?style=flat)](https://landscape.io/github/bmd/pyOptimizely/master)

A minimal python wrapper for the Optimizely REST API.

_Note:_ This project has become more of a demo for correctly building a Python application that utilizes a Travis/Coveralls CI stack. It's _way_ overengineered for what it is an you should use something like [Tortilla](https://pypi.python.org/pypi/tortilla) for wrapping a simple REST API like Optimizely's.

### Example

```py
from optimizely import Optimizely

OPTIMIZELY_TOKEN = 'abc123'

opt = Optimizely(OPTIMIZELY_TOKEN)
experiments = opt.get('/experiments').json()

print(json.dumps(experiments, indent=2))
```