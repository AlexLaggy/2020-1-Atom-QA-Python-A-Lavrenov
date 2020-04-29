import requests


class ResponseStatusCodeException(Exception):
    pass


class RequestErrorException(Exception):
    pass


class ApiClient:

    def __init__(self, user, password):
        self.login_url = 'https://account.my.com'
        self.base_url = 'https://target.my.com'

        self.session = requests.Session()
        self.csrf_token = None

        self.segment_id = None

        self.user = user
        self.password = password
        self.login()

    def login(self):
        location_auth = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
        location_csrf = 'https://target.my.com/csrf'

        headers = {
            'Referer': 'https://target.my.com/'
        }

        data = {
            'email': self.user,
            'password': self.password
        }
        self.session.request('POST', location_auth, headers=headers, data=data, allow_redirects=False)
        self.session.request('GET', location_csrf, headers=headers, json=True)
        self.csrf_token = requests.utils.dict_from_cookiejar(self.session.cookies)['csrftoken']

    def check_segment(self, segment_id):
        location = f'https://target.my.com/segments/segments_list/{segment_id}'
        headers = {
            'Referer': 'https://target.my.com/segments/segments_list'
        }
        response = self.session.request('GET', location, headers=headers)
        return response, location

    def delete_segment(self, segment_id):
        location = f'https://target.my.com/api/v2/remarketing/segments/{segment_id}.json'
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Referer': 'https://target.my.com/segments/segments_list'
        }
        return self.session.request('DELETE', location, headers=headers)

    def create_segment(self, segment_name="TestApi"):
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Referer': 'https://target.my.com/segments/segments_list/new',
        }
        create_segment_json = {"name": segment_name,
                               "pass_condition": 1,
                               "relations": [
                                  {"object_type": "remarketing_users_list",
                                   "params": {
                                       "source_id": 9847753,
                                       "type": "positive"}
                                   }
                               ],
                               "logicType": "or"}
        location = 'https://target.my.com/api/v2/remarketing/segments.json?fields=relations__object_type,' \
                   'relations__object_id,relations__params,relations_count,id,name,' \
                   'pass_condition,created,campaign_ids,users,flags'
        response = self.session.request('POST', location, headers=headers, json=create_segment_json)
        return response
