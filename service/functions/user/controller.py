from typing import List, Union
from repository import UserRepository
from summary import UserSummary


class UserController:
    def __init__(self, repository: UserRepository):
        self.__repository = repository

    def __getMultiple(self, event: dict) -> List[dict]:
        users = self.__repository.objects()
        return list(map(lambda user: UserSummary(user).asDict(), users))

    def __getOne(self, event: dict) -> dict:
        user = self.__repository.object(event["objectId"])
        return UserSummary(user).asDict()

    def get(self, event: dict) -> Union[List[dict], dict]:
        if event.get("objectId") is None:
            return self.__getMultiple(event)
        return self.__getOne(event)

    def post(self, event: dict) -> dict:
        user = self.__repository.create(event["object"])
        return UserSummary(user).asDict()
