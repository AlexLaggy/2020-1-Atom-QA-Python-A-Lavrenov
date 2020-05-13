import threading

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker, mapper
from flask import Flask, request, abort

app = Flask(__name__)


class Users(object):
    pass


class DBUser:
    def __init__(self, login, password, db, host, port):
        self.host = host
        self.port = port
        self.db = db
        self.login = login
        self.password = password
        self.table = Users
        self.session = self.connect()

    def connect(self):
        url = f'mysql+pymysql://{self.login}:{self.password}@{self.host}:{self.port}/{self.db}'

        engine = create_engine(url)
        metadata = MetaData(engine)
        test_users = Table('test_users', metadata, autoload=True)
        mapper(Users, test_users)

        session = sessionmaker(bind=engine, autocommit=True, enable_baked_queries=False)

        return session()


def run_mock(host, port):
    server = threading.Thread(target=app.run, kwargs={'host': host, 'port': port})
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


def db_select(self, field, value):
    self.db.session.expire_all()
    return self.db.session.query(self.db.table).filter(field == value).first()


@app.route('/vk_id/<username>')
def get_vk_id(username: str):
    a.session.expire_all()
    user = a.session.query(a.table).filter(a.table.username == username).first()
    if user:
        return {'vk_id': user.id}, 200
    else:
        abort(404)


@app.route('/shutdown')
def shutdown():
    shutdown_mock()


if __name__ == '__main__':
    run_mock('0.0.0.0', 5000)
    a = DBUser('mock', 'mock', 'test', 'mysql_database', '3306')
