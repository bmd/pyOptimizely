import context
from optimizely import Optimizely
import requests
import pytest


def test_instantiates_optimizely():
    opt = Optimizely('abc123')
    assert isinstance(opt, Optimizely)


def test_bad_credentials_raise_exception():
    with pytest.raises(requests.HTTPError):
        Optimizely('abc123').get('/experiments/123').raise_for_status()

