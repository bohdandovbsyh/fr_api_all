import requests


class BaseAPI:

    def __init__(self, env_class):
        self.__base_url = env_class.base_api
        self.__headers = {'Accept': '*/*', 'Content-Type': 'application/json'}
        self.__request = requests

    def get(self, url, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.get(f'{self.__base_url}{url}', headers=headers)
        return response

    def post(self, url, body, headers=None):
        if headers is None:
            headers = self.__headers
        resource = self.__request.post(f'{self.__base_url}{url}', json=body, headers=headers)
        return resource

    def put(self):
        ...

    def delete(self):
        ...

    def patch(self):
        ...
