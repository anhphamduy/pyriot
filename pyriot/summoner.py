class SummonerApi:

    def __init__(self, client):
        self.client = client

    def get_by_encrypted_account_id(self, encrypted_account_id):
        raise NotImplementedError()

    def get_by_name(self, name):
        raise NotImplementedError()

    def get_by_puuid(self, puuid):
        raise NotImplementedError()

    def get_by_encrypted_summoner_id(self, summoner_id):
        raise NotImplementedError()

    def get_me(self):
        raise NotImplementedError()

    def _get_from_response(self):
        raise NotImplementedError()


class Summoner:
    pass
