from sqlalchemy.orm import sessionmaker
from orm.create_db import engine, Base
from orm.models import Size, Client, Server

Session = sessionmaker(bind=engine)
session = Session()


def add_to_size_table(arr):
    results = []
    for raw in arr:
        results.append(Size(ip=raw['ip'], method=raw['method'], url=raw['url'], time=raw['time'], size=raw['size']))
    if len(results):
        print(results)
        session.add_all(results)


def add_to_client_table(arr):
    results = []
    for raw in arr:
        results.append(Client(ip=raw['ip'], method=raw['method'], url=raw['url'], status_code=raw['status']))
    if len(results):
        session.add_all(results)


def add_to_server_table(arr):
    results = []
    for raw in arr:
        results.append(Server(ip=raw['ip'], method=raw['method'], url=raw['url'], status_code=raw['status']))
    if len(results):
        session.add_all(results)

