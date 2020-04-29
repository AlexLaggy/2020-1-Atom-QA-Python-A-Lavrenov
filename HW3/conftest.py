import pytest
import requests
import os
from orm.fixtures import *
from linux.connector import SSH
from mock import mock
from socket_client.socket_client import MySocket
from orm.create_db import DBUser


class UsupportedBrowserException(Exception):
    pass


@pytest.fixture(scope='session')
def config():
    host = '127.0.0.1'
    port = 5000
    linux_host = '192.168.1.46'
    linux_port = 2222
    http_port = 8080
    username = 'centos'
    password = 'centos'
    db_name = 'ormdata'
    db_login = 'admin'
    db_host = 'localhost'
    db_password = 'password'
    path_dir_orm = '/'.join(os.path.dirname(os.path.realpath(__file__)).split('/'))
    file_orm = 'access.log'
    return {'host': host, 'port': port, 'linux_port': linux_port, 'linux_host': linux_host, 'file_orm': file_orm,
            'http_port': http_port, 'username': username, 'password': password, 'db_host': db_host,
            'db_name': db_name, 'db_login': db_login, 'db_password': db_password, 'path_dir_orm': path_dir_orm}


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


@pytest.fixture(scope='session')
def linux_client(config):
    with SSH(hostname=config['linux_host'], username=config['username'], password=config['password'],
             port=config['linux_port'], http_port=config['http_port']) as host:
        yield host


@pytest.fixture(scope='session')
def db_client(config):
    return DBUser(login=config['db_login'], password=config['db_password'], file=config['file_orm'],
                  db=config['db_name'], host=config['db_host'], path_dir=config['path_dir_orm'])
