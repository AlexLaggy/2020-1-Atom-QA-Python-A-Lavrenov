import pytest

from orm.models import Client


@pytest.fixture(scope='function')
def orm_client():
    return Client
