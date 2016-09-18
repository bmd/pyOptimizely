import json
import requests
from typing import Dict


class Optimizely:
    """ A Python wrapper around the Optimizely REST API """

    api_base_url = 'https://www.optimizelyapis.com/experiment/v1/{endpoint}'

    def __init__(self, token: str) -> None:
        """ Create an Optimizely object.

        The init method just sets a token so that later calls can re-uuse the
        same credentials without passing in the authentication token
        specifically.

        Args:
            token: (string). A valid token for the Optimizely REST API. If you
            don't already have a token, you can generate one using the
            documentation provided by Optimizely.

        References:
            Optimizely REST API documentation:
            https://developers.optimizely.com/rest/introduction/index.html
        """
        self.token = token

    def _call(self, method: callable, endpoint: str, data: Dict = None) -> Dict:
        """ Generic method for calling the Optimizely API.

        Abstracts any required plumbing for the optimizely API (in thie case,
        assembling the complete request URI and setting the authentication
        token in the header) to ensure that behavior is consistent across
        HTTP verbs.

        The _call method should not be invoked directly. Use the convenience
        methods .get, .post, .put, and .delete for a more semantic interface.

        Args:
            method: (callable)
            endpoint: (sting)
            data: (dict|None) The body of the request (not applicable for GET
            and DELETE requests).

        Returns:
            A dictionary object representing the serialized response from the
            Optimizely API.
        """
        header = {'Token': self.token}

        if data:
            header['content-type'] = 'application/json'
            data = json.dumps(data)

        uri = Optimizely.api_base_url.format(endpoint=endpoint)
        response = method(uri, headers=header, data=data)

        return response.json()

    def get(self, endpoint: str) -> Dict:
        """ A semantic wrapper for GET requests.

        Args:
            endpoint: (string) The endpoint to make a request to, not including
            the Base URI. For example: '/experiments/123'

        Returns:
            A dictionary object representing the serialized response from the
            Optimizely API.
        """
        return self._call(requests.get, endpoint)

    def post(self, endpoint: str, data: Dict) -> Dict:
        """ Semantic wrapper for POST requests to the Optimizely REST API.

        Args:
            endpoint: (string) The endpoint to make a request to, not including
            the Base URI. For example: '/experiments/123'
            data: (dict) A json-serializeable object to be encoded in the request
            body.

        Returns:
            A dictionary object representing the serialized response from the
            Optimizely API.
        """
        return self._call(requests.post, endpoint, data=data)

    def put(self, endpoint: str, data: Dict) -> Dict:
        """ Semantic wrapper for PUT requests to the Optimizely REST API.

        Args:
            endpoint: (string) The endpoint to make a request to, not including
            the Base URI. For example: '/experiments/123'
            data: (dict) A json-serializeable object to be encoded in the request
            body.

        Returns:
            A dictionary object representing the serialized response from the
            Optimizely API.
        """
        return self._call(requests.put, endpoint, data=data)

    def delete(self, endpoint: str) -> Dict:
        """ Semantic wrapper for DELETE requests to the Optimizely REST API.

        Args:
            endpoint: (string) The endpoint to make a request to, not including
            the Base URI. For example: '/experiments/123'

        Returns:
            A dictionary object representing the serialized response from the
            Optimizely API.
        """
        return self._call(requests.delete, endpoint)
