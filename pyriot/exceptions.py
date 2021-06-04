class RiotRequestException(Exception):
    def __init__(self, message, response):
        super().__init__(message)

        self.response = response


class SummonerNotFound(Exception):
    pass


class DataclassMappingMismatchException(Exception):
    def __init__(self, dataclass, actual_annotations):
        super().__init__(f'dataclass {dataclass.__annotations__} does not match ${actual_annotations}')
