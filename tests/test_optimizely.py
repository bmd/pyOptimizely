import context
from optimizely import Optimizely
import requests
import pytest
import os

OPTIMIZELY_KEY = os.getenv('OPTIMIZELY_API_KEY')


def test_instantiates_optimizely():
    opt = Optimizely('abc123')
    assert isinstance(opt, Optimizely)


def test_bad_credentials_raise_exception():
    with pytest.raises(requests.HTTPError):
        Optimizely('abc123').get('/experiments/123').raise_for_status()


def test_authenticates_with_credentials():
    response = Optimizely(OPTIMIZELY_KEY).get('/projects')
    assert response.status_code == 200


def test_gets_single_project():
    response = Optimizely(OPTIMIZELY_KEY).get('/projects/147884460')
    assert response.status_code == 200
    assert response.json()['project_name'] == 'Rainforest Alliance'


def test_updates_project():
    response = Optimizely(OPTIMIZELY_KEY).put('/projects/147884460/', data={'ip_filter': None})
    assert response.status_code == 202
    assert not response.json()['ip_filter']


def test_creates_and_deletes_experiments():
    """
curl \
  -H "Token: abcdefghijklmnopqrstuvwxyz:123456" \
  -H "Content-Type: application/json" \
  -d '{"edit_url":"https://mysite.com/products/","description":"My Experiment Name"}' \
  "https://www.optimizelyapis.com/experiment/v1/projects/1234/experiments/"


    """
