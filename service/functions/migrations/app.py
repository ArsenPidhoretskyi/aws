from os import environ

from alembic import command
from alembic.config import Config


def lambda_handler(event, context):
    connectionString = environ["DB_CONNECTION_STRING"]

    config = Config('alembic.ini')
    config.set_main_option('prepend_sys_path', '.')
    config.set_main_option('sqlalchemy.url', connectionString)

    command.upgrade(config, 'head')
