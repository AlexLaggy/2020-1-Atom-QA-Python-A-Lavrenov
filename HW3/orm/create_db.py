from sqlalchemy import create_engine
from orm.models import Base
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker


class DBUser:
    def __init__(self, login, password, db, host, path_dir, file):
        self.login = login
        self.password = password
        self.db = db
        self.host = host
        self.session = None
        self.path_dir = path_dir
        self.file = file

    def create_db(self):
        url = f'mysql+pymysql://{self.login}:{self.password}@{self.host}/{self.db}'

        if not database_exists(url):
            create_database(url)

        engine = create_engine(url)

        Session = sessionmaker(bind=engine)
        self.session = Session()

        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
