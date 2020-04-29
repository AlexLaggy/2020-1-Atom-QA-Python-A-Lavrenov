from orm.models import Size, Client, ClientSize


def add_to_size_table(arr, session):
    results = []
    for raw in arr:
        results.append(Size(ip=raw['ip'], method=raw['method'], url=raw['url'], time=raw['time'], size=raw['size']))
    if len(results):
        session.add_all(results)


def add_to_client_table(arr, session):
    results = []
    for raw in arr:
        results.append(Client(ip=raw['ip'], method=raw['method'], url=raw['url'],
                              status_code=raw['status'], count=raw['count']))
    if len(results):
        session.add_all(results)


def add_to_server_table(arr, session):
    results = []
    for raw in arr:
        results.append(ClientSize(ip=raw['ip'], method=raw['method'], url=raw['url'],
                                  status_code=raw['status'], size=raw['size']))
    if len(results):
        session.add_all(results)
