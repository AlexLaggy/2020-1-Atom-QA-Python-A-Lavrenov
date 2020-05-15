import pytest

from tests.base_api import BaseCase

# 308 redirect=False to Home
# after registration to reg
# reg 500 при первой регистрации Akkakiy13


class TestApi(BaseCase):
    def db_select(self, field, value):
        self.db.session.expire_all()
        return self.db.session.query(self.db.table).filter(field == value).first()

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    @pytest.mark.parametrize('url', ['static/images/laptop.png', 'static/scripts/findMeError.js'])
    def test_find_me_error(self, url):
        response = self.api_client.get(url)
        assert response.status_code == 200  # TODO: нашел findMeError.js

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    def test_login(self):
        response = self.api_client.login(self.api_client.user, self.api_client.password)
        assert response.status_code == 200

        result = self.db_select(self.db.table.username, self.api_client.user)
        assert result.active == 1

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    @pytest.mark.parametrize('username, password', [('Arto', 'p')])
    def test_login_error_200(self, username, password):
        response = self.api_client.login(username, password)
        assert response.status_code == 401  # TODO: код ошибки 200, а должен быть 401

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    def test_logout(self):
        response = self.api_client.login(self.api_client.user, self.api_client.password)
        assert response.status_code == 200

        result = self.db_select(self.db.table.username, self.api_client.user)
        assert result.active == 1

        response = self.api_client.logout()
        assert response.status_code == 200

        result = self.db_select(self.db.table.username, self.api_client.user)
        assert result.active == 0

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    def test_login_500(self):
        response = self.api_client.login(self.api_client.user, self.api_client.password)
        assert response.status_code == 200

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    def test_add_user(self):
        response = self.api_client.add_user('FastTest', 'qwe', 'test@test.te')
        assert response.status_code == 201  # TODO: add_user - не работает api

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    @pytest.mark.parametrize('username,email,password', [('Artourchik', 'awp@top.co', 'p')])
    def test_del_user(self, username, email, password):
        response = self.api_client.reg(username, email, password, password)
        assert response.status_code == 200

        result = self.db_select(self.db.table.username, username)
        assert result.username == username

        response = self.api_client.del_user(username)
        assert response.status_code == 204

        result = self.db_select(self.db.table.username, username)
        assert result is None

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    def test_del_user_error(self):
        self.api_client.login(self.api_client.user, self.api_client.password)

        response = self.api_client.del_user('Ar')
        assert response.status_code == 404 and response.content == b'User does not exist!'

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    @pytest.mark.parametrize('username,email,password', [('Kadzima', 'kad@zi.ma', 'p')])
    def test_block_user(self, username, email, password):
        self.api_client.reg(username, email, password, password)

        self.api_client.login(username, password)

        self.api_client.block_user(username)

        result = self.db_select(self.db.table.username, username)
        assert result.access == 0

        self.api_client.del_user(username)
        assert result.active == 0  # TODO: при блоке - active не сбрасявыется

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    def test_block_user_bad(self):
        self.api_client.login(self.api_client.user, self.api_client.password)

        response = self.api_client.block_user('FastCrack')
        assert response.status_code == 404 and response.content == b'User does not exist!'

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    @pytest.mark.parametrize('username,email,password', [('Zeleboba', 'ulica@zi.ma', 'p')])
    def test_block_user_304(self, username, email, password):
        self.api_client.reg(username, email, password, password)

        self.api_client.login(self.api_client.user, self.api_client.password)

        response = self.api_client.block_user(username)
        assert response.status_code == 200

        self.api_client.del_user(username)

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    @pytest.mark.parametrize('username,email,password', [('AlexPistoletov', 'alex@pist.ov', 'p')])
    def test_unblock_user(self, username, email, password):
        self.api_client.reg(username, email, password, password)

        self.api_client.login(self.api_client.user, self.api_client.password)

        response = self.api_client.block_user(username)
        assert response.status_code == 304

        result = self.db_select(self.db.table.username, username)
        assert result.access == 0

        response = self.api_client.unblock_user(username)
        assert response.status_code == 200

        result = self.db_select(self.db.table.username, username)
        assert result.access == 1

        self.api_client.del_user(username)

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    def test_unblock_user_bad(self):
        self.api_client.login(self.api_client.user, self.api_client.password)

        response = self.api_client.unblock_user('FastCrack')
        assert response.status_code == 404 and response.content == b'User does not exist!'

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    def test_get_status(self):
        response = self.api_client.status()
        assert response.status_code == 200

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    @pytest.mark.parametrize('username,email,password', [('Pontalika', 'aw@top.co', 'p')])
    def test_reg(self, username, email, password):
        response = self.api_client.reg(username, email, password, password)
        assert response.status_code == 200

        result = self.db_select(self.db.table.username, username)
        assert result.username == username

        self.api_client.del_user(username)

        result = self.db_select(self.db.table.username, username)
        assert result is None

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    @pytest.mark.parametrize('username,email,password', [('Repeted', 'yay@yas.ru', 'p')])
    def test_reg_repeated_email(self, username, email, password):
        response = self.api_client.reg(username, email, password, password)

        assert response.status_code == 400  # TODO: сервер выдает 500

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    @pytest.mark.parametrize('username,email,password', [('Akkakiy13', 'yy@yas.ru', 'p')])
    def test_reg_409(self, username, email, password):
        response = self.api_client.reg(username, email, password, password)

        assert response.status_code == 400  # TODO: нету ответа 409 в описании
