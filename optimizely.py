import json
import requests


class Optimizely:
    """ Minimal Optimizely API class """
    def __init__(self, token, strict=True):
        self.token = token
        self.settings = {
            'strict': strict
        }

    def _call(self, method, endpoint, callback=None, data=None):
        header = {
            'Token': self.token
        }

        if data:
            header['content-type'] = 'application/json'
            data = json.dumps(data)
        uri = 'https://www.optimizelyapis.com/experiment/v1/{e}'.format(e=endpoint)
        response = method(uri, headers=header, data=data)

        if self.settings['strict']:
            response.raise_for_status()

        return callback(response.json()) if callback else response.json()

    def get(self, endpoint, callback=None):
        return self._call(requests.get, endpoint, callback)

    def put(self, endpoint, data, callback=None):
        return self._call(requests.put, endpoint, callback, data=data)

    def post(self, endpoint, data, callback=None):
        return self._call(requests.post, endpoint, callback, data=data)

    def delete(self, endpoint, callback=None):
        return self._call(requests.delete, endpoint, callback)
