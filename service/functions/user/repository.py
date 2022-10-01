from typing import List
from sqlalchemy.orm.session import Session

from models import User


class UserRepository:
    def __init__(self, session: Session):
        self.__session = session

    def __del__(self):
        self.__session.close()

    def object(self, objectId: int) -> User:
        return self.__session.query(User).filter_by(id=objectId).one()

    def objects(self) -> List[User]:
        return self.__session.query(User).all()

    def create(self, properties: dict) -> User:
        user = User(**properties)
        self.__session.add(user)
        self.__session.commit()
        self.__session.refresh(user)
        return user
