from dataclasses import dataclass

from pyriot.api import ApiModel, RiotApi
from pyriot.exceptions import RiotRequestException, SummonerNotFound


@dataclass
class Summoner(ApiModel):
    name: str

    def __init__(self):
        pass


class SummonerApi(RiotApi):
    BASE_SNIPPET = 'lol/summoner/v4/summoners/'

    ACCOUNT_ID_SNIPPET = 'by-account/'
    NAME_SNIPPET = 'by-name/'
    PUUID_SNIPPET = 'by-uuid/'
    ME_SNIPPET = 'me/'

    def __init__(self, client):
        self.client = client

    def get_by_encrypted_account_id(self, encrypted_account_id):
        url = self.BASE_SNIPPET + self.ACCOUNT_ID_SNIPPET + encrypted_account_id
        return self._get(url)

    def get_by_name(self, name):
        url = self.BASE_SNIPPET + self.NAME_SNIPPET + name
        return self._get(url)

    def get_by_puuid(self, puuid):
        url = self.BASE_SNIPPET + self.PUUID_SNIPPET + puuid
        return self._get(url)

    def get_by_encrypted_summoner_id(self, summoner_id):
        url = self.BASE_SNIPPET + summoner_id
        return self._get(url)

    def get_me(self):
        url = self.BASE_SNIPPET + self.ME_SNIPPET
        return self._get(url)

    def _get(self, url):
        try:
            response = self.client.get(url)
        except RiotRequestException as e:
            response = e.response

            if response.status_code == 404:
                raise SummonerNotFound()

        return self._get_from_response(response)

    def _get_from_response(self, response):
        return super()._get_from_response(response)

    class Meta:
        model = Summoner
