import pytest

from tests.base_api import BaseCase

# 308 redirect=False to Home
# after registration to reg
# reg 500 при первой регистрации Akkakiy13

# внутри Jenkins поднимать docker-compose (+)
# Создать фикстуру для пользователя DB (+)
# Данные для тестов в Faker (?)
# Timeout для selenoid (+)
# Вернуть скриншоты, но только на UI (+)
# Многопоточный запуск тест


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
    # @pytest.mark.parametrize('username, password', [(data[0]['username'], data[0]['password'])])
    # @pytest.mark.usefixtures("parametrized_fixture")
    def test_login_error_200(self, parametrized_fixture):
        username, _, password = parametrized_fixture.values()
        response = self.api_client.login(username[:4], password)

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
    # @pytest.mark.parametrize('username,email,password', [(data[1].values())])
    # @pytest.mark.usefixtures("parametrized_fixture")
    def test_add_user(self, parametrized_fixture):
        username, email, password = parametrized_fixture.values()
        self.api_client.login(self.api_client.user, self.api_client.password)
        response = self.api_client.add_user(username, password, email)

        self.api_client.del_user(username)

        assert response.status_code == 201  # TODO: код добавления от сервера 210, а должен быть 201

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    # @pytest.mark.parametrize('username,email,password', [(data[2].values())])
    def test_del_user(self, parametrized_fixture):
        username, email, password = parametrized_fixture.values()
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
    # @pytest.mark.parametrize('username,email,password', [(data[3].values())])
    def test_block_user(self, parametrized_fixture):
        username, email, password = parametrized_fixture.values()
        self.api_client.reg(username, email, password, password)

        self.api_client.login(self.api_client.user, self.api_client.password)

        self.api_client.block_user(username)

        result = self.db_select(self.db.table.username, username)
        assert result.access == 0
        # print(result.__dict__)
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
    # @pytest.mark.parametrize('username,email,password', [(data[4].values())])
    def test_block_user_304(self, parametrized_fixture):
        username, email, password = parametrized_fixture.values()
        self.api_client.reg(username, email, password, password)

        self.api_client.login(self.api_client.user, self.api_client.password)

        response = self.api_client.block_user(username)
        self.api_client.del_user(username)
        assert response.status_code == 200

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    # @pytest.mark.parametrize('username,email,password', [(data[5].values())])
    def test_unblock_user(self, parametrized_fixture):
        username, email, password = parametrized_fixture.values()
        self.api_client.reg(username, email, password, password)

        self.api_client.login(self.api_client.user, self.api_client.password)

        self.api_client.block_user(username)

        result = self.db_select(self.db.table.username, username)
        assert result.access == 0

        self.api_client.unblock_user(username)

        self.api_client.del_user(username)
        assert result.access == 1

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
    # @pytest.mark.parametrize('username,email,password', [(data[6].values())])
    def test_reg(self, parametrized_fixture):
        username, email, password = parametrized_fixture.values()
        response = self.api_client.reg(username, email, password, password)
        assert response.status_code == 200

        result = self.db_select(self.db.table.username, username)
        assert result.username == username

        self.api_client.del_user(username)

        result = self.db_select(self.db.table.username, username)
        assert result is None

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    # @pytest.mark.parametrize('username,password', [(data[7]['username'], data[7]['password'])])
    def test_reg_repeated_email(self, parametrized_fixture):
        username, _, password = parametrized_fixture.values()
        response = self.api_client.reg(username, self.api_client.email, password, password)
        assert response.status_code == 400  # TODO: сервер выдает 500

    @pytest.mark.API
    # @pytest.mark.skip("TEMP")
    # @pytest.mark.parametrize('username,email,password', [(data[0]['username'], data[8]['email'],
    # data[8]['password'])])
    def test_reg_409(self, parametrized_fixture):
        username, email, password = parametrized_fixture.values()
        response = self.api_client.reg(self.api_client.user, email, password, password)

        self.api_client.del_user(username)

        assert response.status_code == 400  # TODO: нету ответа 409 в описании
