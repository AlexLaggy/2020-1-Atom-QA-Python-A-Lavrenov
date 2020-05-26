from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker, mapper


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

        session = sessionmaker(bind=engine, autocommit=True, enable_baked_queries=False, expire_on_commit=False)

        return session()


if __name__ == '__main__':
    a = DBUser('test_qa', 'qa_test', 'test', '0.0.0.0', '3306')
    for item in a.session.query(a.table).all():
        print(item.__dict__)
