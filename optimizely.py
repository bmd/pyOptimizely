import json
import requests


class Optimizely:
    """ A Python wrapper around the Optimizely REST API

    Attributes
        _token (str): The Optimizely API token passe in the class constructor.
        _api_base_url (str): The Base URL for the Optimizely API. Hardcoded as
            it is unlikely to change, but if the API reaches a 'v2' designation,
            it could be appropriate to add support for the v1 and v2 APIs within
            a single class.
    """

    def __init__(self, token):
        """ Create an Optimizely object.

        The init method just sets a token so that later calls can re-use the
        same credentials without passing in the authentication token
        explicitly.

        Args:
            token (str): A valid token for the Optimizely REST API. If you
                don't already have a token, you can generate one using the
                documentation provided by Optimizely.

        References:
            Optimizely REST API documentation:
            https://developers.optimizely.com/rest/introduction/index.html
        """
        self._api_base_url = 'https://www.optimizelyapis.com/experiment/v1{endpoint}'
        self._token = token

    def _call(self, method, endpoint, data=None):
        """ Generic method for calling the Optimizely API.

        Abstracts any required plumbing for the optimizely API (in thie case,
        assembling the complete request URI and setting the authentication
        token in the header) to ensure that behavior is consistent across
        HTTP verbs.

        The _call method should not be invoked directly. Use the convenience
        methods .get, .post, .put, and .delete for a more semantic interface.

        Args:
            method (callable): A http method from the `requests` library.
            endpoint (sting): The Optimizely REST API endpoint to make the
                request to. Combined with the method parameter, this will
                be a unique operation, meaning that you can wrap this method,
                or one of its decendendants in a `partial` to encourage simple
                re-use of a single endpoint with multiple payloads.

        Keyword Args:
            data: (dict|None) The body of the request (not applicable for GET
            and DELETE requests).

        Returns:
            requests.response
        """
        headers = {
            'Token': self._token
        }

        if data:
            # specify that body is being sent as JSON
            headers['content-type'] = 'application/json'
            data = json.dumps(data)

        uri = self._api_base_url.format(endpoint=endpoint)
        response = method(uri, headers=headers, data=data)

        return response

    def get(self, endpoint):
        """ A semantic wrapper for GET requests.

        Args:
            endpoint: (string) The endpoint to make a request to, not including
            the Base URI. For example: '/experiments/123'

        Returns:
            requests.response
        """
        return self._call(requests.get, endpoint)

    def post(self, endpoint, data):
        """ Semantic wrapper for POST requests to the Optimizely REST API.

        Args:
            endpoint: (string) The endpoint to make a request to, not including
            the Base URI. For example: '/experiments/123'
            data: (dict) A json-serializeable object to be encoded in the request
            body.

        Returns:
            requests.Response The response object.
        """
        return self._call(requests.post, endpoint, data=data)

    def put(self, endpoint, data):
        """ Semantic wrapper for PUT requests to the Optimizely REST API.

        Args:
            endpoint: (string) The endpoint to make a request to, not including
            the Base URI. For example: '/experiments/123'
            data: (dict) A json-serializeable object to be encoded in the request
            body.

        Returns:
            requests.Response The response object.
        """
        return self._call(requests.put, endpoint, data=data)

    def delete(self, endpoint):
        """ Semantic wrapper for DELETE requests to the Optimizely REST API.

        Args:
            endpoint: (string) The endpoint to make a request to, not including
            the Base URI. For example: '/experiments/123'

        Returns:
            requests.Response The response object.
        """
        return self._call(requests.delete, endpoint)
