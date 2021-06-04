import re

from pyriot.exceptions import DataclassMappingMismatchException


class RiotApi:
    @classmethod
    def _get_from_response(cls, response):
        instance = cls.Meta.model()

        # transform the response keys from camel case to snake case
        snake_case_response = {}
        for key, value in response.items():
            snake_case_response[cls._convert_camel_case(key)] = value

        if not cls._verify_dataclass_model_mapping(instance, snake_case_response):
            raise DataclassMappingMismatchException(instance, snake_case_response)

        # copy the data to the object when the data is of a expected format
        for key, value in snake_case_response.items():
            setattr(instance, key, value)

        return instance

    @staticmethod
    def _verify_dataclass_model_mapping(model, key_mapping):
        return set(model.__annotations__) == set(key_mapping)

    @staticmethod
    def _convert_camel_case(case):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', case).lower()


class ApiModel:
    def _get_from_response(self, response):
        self.__dict__.update(response)
