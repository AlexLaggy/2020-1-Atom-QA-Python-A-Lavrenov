import pytest

from bash.scripting import Scripts
from orm.go_log import *


class TestDB:

    def db_insert(self, client):
        client.create_db()
        s = Scripts()
        s.read_file(client.path_dir, client.file)
        add_to_size_table(s.top_size, client.session)
        add_to_client_table(s.top_client, client.session)
        add_to_server_table(s.top_client_size, client.session)
        client.session.commit()

    @pytest.mark.ORM
    def test_db(self, orm_client, db_client):
        self.db_insert(db_client)
        clients = db_client.session.query(orm_client).all()
        db_client.session.close()
        assert len(clients) == 10
