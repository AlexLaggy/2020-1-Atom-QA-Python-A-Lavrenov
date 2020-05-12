import pytest

from DB.connector import DBUser


class UsupportedBrowserException(Exception):
    pass


@pytest.fixture(scope='session')
def db_user(config):
    return DBUser(config['db_user'], config['db_password'], config['db_name'],
                  config['db_host'], config['db_port'])
