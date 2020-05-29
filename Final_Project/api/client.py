import requests
import json


class ResponseStatusCodeException(Exception):
    pass


class RequestErrorException(Exception):
    pass


class ApiClient:

    def __init__(self, user, password, email, url):
        self.base_url = url

        self.session = requests.Session()

        self.user = user
        self.password = password
        self.email = email

    def get(self, url):
        return self.session.request('GET', f'{self.base_url}/{url}')

    def login(self, user, password):
        data = {
            "username": user,
            "password": password,
            "submit": "Login"
        }
        return self.session.request('POST', f'{self.base_url}/login', data=data)

    def logout(self):
        return self.session.request('GET', f'{self.base_url}/logout')

    def add_user(self, username, email, password):

        data = {
            "username": username,
            "password": password,
            "email": email
        }
        return self.session.request('POST', f'{self.base_url}/api/add_user', data=json.dumps(data))

    def del_user(self, username):
        return self.session.request('GET', f'{self.base_url}/api/del_user/{username}')

    def block_user(self, username):
        return self.session.request('GET', f'{self.base_url}/api/block_user/{username}')

    def unblock_user(self, username):
        return self.session.request('GET', f'{self.base_url}/api/accept_user/{username}')

    def status(self):
        return self.session.request('GET', f'{self.base_url}/status')

    def reg(self, username, email, password, confirm):
        data = {
            "username": username,
            "email": email,
            "password": password,
            "confirm": confirm,
            "term": "y",
            "submit": "Register"
        }
        return self.session.request('POST', f'{self.base_url}/reg', data=data)
