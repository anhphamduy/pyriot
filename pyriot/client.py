import requests
import json

from .exceptions import RiotRequestException


class RiotClient:
    RIOT_BASE_URL = 'https://oc1.api.riotgames.com/'
    RIOT_AUTH_TOKEN_HEADER_KEY = 'X-Riot-Token'

    GET_METHOD = 'GET'
    POST_METHOD = 'POST'

    ERROR_STATUS_CODE_BOUNDARY = 400
    ERROR_RESPONSE_MESSAGE = 'Status code is not ok'

    def __init__(self, token):
        self.token = token

    def get(self, snippet):
        response = requests.get(self.RIOT_BASE_URL + snippet, headers=self.headers)

        if response.status_code > self.ERROR_STATUS_CODE_BOUNDARY:
            raise RiotRequestException(self.ERROR_RESPONSE_MESSAGE, response)

        return json.loads(response.content)

    @staticmethod
    def _get_response_from_connection(connection):
        return connection.getresponse().read().decode()

    @property
    def headers(self):
        return {
            self.RIOT_AUTH_TOKEN_HEADER_KEY: self.token,
        }
