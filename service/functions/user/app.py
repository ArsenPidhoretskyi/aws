from os import environ
from typing import Optional
from sqlalchemy.engine import create_engine, Engine
from sqlalchemy.orm.session import sessionmaker
from repository import UserRepository
from controller import UserController


class App:
    def __init__(self, engine: Engine):
        self.__engine = engine
        self.__sessionmaker = sessionmaker(bind=self.__engine)

    def run(self, event: dict):
        repository = UserRepository(self.__sessionmaker())
        controller = UserController(repository)

        METHODS = {
            "GET": controller.get,
            "POST": controller.post
        }

        return METHODS[event["method"].upper()](event)


app: Optional[App] = None


def lambda_handler(event, context):
    global app
    if app is None:
        engine = create_engine(environ["DB_CONNECTION_STRING"])
        app = App(engine)

    return app.run(event)
