import pytest
import requests
from orm.fixtures import *
from mock import mock
from socket_client.socket_client import MySocket


class UsupportedBrowserException(Exception):
    pass


@pytest.fixture(scope='session')
def config():
    host = '127.0.0.1'
    port = 5000
    return {'host': host, 'port': port}


@pytest.fixture(scope='session')
def mock_server(config):
    mock.run_mock(config['host'], config['port'])

    server_host = config['host']
    server_port = config['port']

    yield server_host, server_port

    shutdown_url = f'http://{server_host}:{server_port}/shutdown'
    requests.get(shutdown_url)


@pytest.fixture(scope='session')
def socket_client(config):
    return MySocket(config['host'], config['port'])


