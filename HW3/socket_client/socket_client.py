import socket
import pprint
import time
import json


class MySocket:
    def __init__(self, target_host, target_port):
        self.target_host = target_host
        self.target_port = target_port
        self.data = []
        self.client = None

    def run(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(0.1)
        time.sleep(0.5)
        self.client.connect((self.target_host, self.target_port))

    def get_request(self, params):
        request = f'GET {params} HTTP/1.1\r\nHost:{self.target_host}\r\n\r\n'
        self.client.send(request.encode())

    def post_request(self, params, data):
        info = f'name={data["name"]}&surname={data["surname"]}'
        request = f'POST {params} HTTP/1.1\r\n' \
                  f'Content-Length: {len(info)}\r\n' \
                  f'Content-Type: application/x-www-form-urlencoded\r\n\r\n' \
                  f'{info}'
        self.client.send(request.encode())

    def receive(self):
        tmp = []
        while True:
            data = self.client.recv(4096)
            if data:
                tmp.append(data.decode())
            else:
                break
        splited_result = ''.join(tmp).split()
        if splited_result[1] == '200':
            return {'status_code': int(splited_result[1]), 'headers': ''.join(tmp).splitlines()[:-1],
                    'data': json.loads(splited_result[-1])}
        else:
            return {'status_code': int(splited_result[1]), 'headers': ''.join(tmp).splitlines()[:-1],
                    'data': None}

    def get_data(self):
        pprint.pprint(self.data)


if __name__ == '__main__':
    a = MySocket('127.0.0.1', 5000)
    a.run()
    a.post_request('/users', {'name': 'Alex', 'surname': 'Laggy'})
    a.receive()
    a.get_data()
