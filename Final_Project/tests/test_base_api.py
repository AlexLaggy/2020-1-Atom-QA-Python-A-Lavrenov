import pytest
import time

from tests.base_api import BaseCase


class TestApi(BaseCase):

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    def test_logout(self):
        result = self.db.session.query(self.db.table).filter(self.db.table.username == self.api_client.user).first()
        print(result.__dict__)

        self.api_client.login(self.api_client.user, self.api_client.password)
        time.sleep(5)
        result = self.db.session.query(self.db.table).filter(self.db.table.username == self.api_client.user).first()
        print(result.__dict__)

        response = self.api_client.logout()
        assert response.status_code == 200
        time.sleep(5)

        result = self.db.session.query(self.db.table).filter(self.db.table.username == self.api_client.user).first()
        print(result.__dict__)
        assert result.active == 0

    @pytest.mark.API
    @pytest.mark.skip("TEMP")
    def test_login(self):
        response = self.api_client.login(self.api_client.user, self.api_client.password)
        assert response.status_code == 200

        result = self.db.session.query(self.db.table).filter(self.db.table.username == self.api_client.user).first()
        assert result.active == 1

    @pytest.mark.API
    @pytest.mark.skip("TEMP")
    def test_active_false_2_login(self):
        response1 = self.api_client.login(self.api_client.user, self.api_client.password)
        assert response1.status_code == 200

        response2 = self.api_client.login("Fasgen", "qwe")
        assert response2.status_code == 200

        # проверка, что в базе значение у первого залогиненного active = True
        result_1 = self.db.session.query(self.db.table).filter(self.db.table.username == self.api_client.user).first()
        result_2 = self.db.session.query(self.db.table).filter(self.db.table.username == "Fasgen").first()

        print(result_2.__dict__, result_1.__dict__)

        assert result_2.active == 1
        assert result_1.active == 0

    @pytest.mark.API
    @pytest.mark.skip("TEMP")
    def test_login_500(self):
        response = self.api_client.login(self.api_client.user, self.api_client.password)
        # print(response.__dict__)
        assert response.status_code == 200

    @pytest.mark.API
    @pytest.mark.skip("TEMP")
    def test_add_user(self):
        response = self.api_client.add_user('FastTest', 'qwe', 'test@test.te')
        print(response.__dict__)
        assert response.status_code == 200

    @pytest.mark.API
    @pytest.mark.skip("TEMP")
    @pytest.mark.parametrize('username', ['Artoure'])
    def test_del_user(self, username):
        time.sleep(1)
        result = self.db.session.query(self.db.table).filter(self.db.table.username == username).all()
        print(result)
        for i in result:
            print(i.__dict__)

        response = self.api_client.del_user(username)
        assert response.status_code == 204

        time.sleep(1)
        result = self.db.session.query(self.db.table).filter(self.db.table.username == username).all()
        print(result)
        for i in result:
            print(i.__dict__)

        time.sleep(1)
        result = self.db.session.query(self.db.table).filter(self.db.table.username == username).all()
        print(result)
        for i in result:
            print(i.__dict__)

        time.sleep(1)
        result = self.db.session.query(self.db.table).filter(self.db.table.username == username).all()
        print(result)
        for i in result:
            print(i.__dict__)
        assert len(result) == 0

    @pytest.mark.API
    @pytest.mark.skip("TEMP")
    def test_del_user_error(self):
        response = self.api_client.del_user('Ar')
        assert response.status_code == 404 and response.content == b'User does not exist!'

    @pytest.mark.API
    @pytest.mark.skip("TEMP")
    def test_block_user(self):
        response = self.api_client.block_user('Fasgas')
        print(response.__dict__)
        assert response.status_code == 200

        # проверка, что при блоке - состояние active остается

    @pytest.mark.API
    @pytest.mark.skip("TEMP")
    def test_block_user_bad(self):
        response = self.api_client.block_user('FastCrack')
        print(response.__dict__)
        assert response.status_code == 404 and response.content == b'User does not exist!'

    @pytest.mark.API
    @pytest.mark.skip("TEMP")
    def test_unblock_user(self):
        response = self.api_client.unblock_user('Fasgas')
        print(response.__dict__)
        assert response.status_code == 200

    @pytest.mark.API
    @pytest.mark.skip("TEMP")
    def test_unblock_user_bad(self):
        response = self.api_client.unblock_user('FastCrack')
        print(response.__dict__)
        assert response.status_code == 404 and response.content == b'User does not exist!'

    @pytest.mark.API
    @pytest.mark.skip("TEMP")
    def test_get_status(self):
        response = self.api_client.status()
        # print(response.__dict__)
        assert response.status_code == 200

    @pytest.mark.API
    @pytest.mark.skip("TEMP")
    def test_reg(self):
        response = self.api_client.reg('Ambassa', 'amb@amba.co', 'p', 'p')
        # print(response.__dict__)
        assert response.status_code == 200

    @pytest.mark.API
    @pytest.mark.skip("TEMP")
    def test_reg_repeated_email(self):
        response = self.api_client.reg('Amba', 'amb@amba.co', 'p', 'p')

        assert response.status_code == 400

    @pytest.mark.API
    @pytest.mark.skip("TEMP")
    def test_reg_409(self):
        response = self.api_client.reg('Ambassador', 'ambas@amba.co', 'p', 'p')

        # No such status in description 409
        assert response.status_code == 400

    @pytest.mark.API
    @pytest.mark.skip("TEMP")
    def test_reg_500(self):
        response = self.api_client.reg('Okulele', 'yy@yas.ru', 'p', 'p')

        # Server Error 500
        assert response.status_code == 200


