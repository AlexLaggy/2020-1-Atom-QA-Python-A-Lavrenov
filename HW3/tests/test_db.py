import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class TestDB:

    @pytest.mark.ORM
    def test_db(self, orm_client):
        engine = create_engine('mysql+pymysql://admin:password@localhost/bash', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        clients = session.query(orm_client).all()
        session.close()
        assert len(clients) == 10

