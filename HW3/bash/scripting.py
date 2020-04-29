import argparse
import os
import json
from itertools import groupby


def parser_addoption(parser):
    parser.add_argument('-d', '--dir', default='/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1]))
    parser.add_argument('-f', '--filename', default=None)


class Scripts:
    def __init__(self):
        self.total_count = 0
        self.type_c = {}
        self.top_size = []
        self.top_client = {}
        self.top_client_size = []

    def pack_to_file(self, file='python_result.csv'):
        with open(file, 'w', newline='\n') as f:
            result = {'total_count': self.total_count,
                      'count_by_type': self.type_c,
                      'top_size': self.top_size[:10],
                      'top_client': self.top_client,
                      'top_client_size': self.top_client_size}
            f.write(json.dumps(result))

    def type_count(self, line):
        method = line.split()[5][1:]
        if method not in self.type_c.keys():
            self.type_c.update({method: 1})
        else:
            self.type_c.update({method: self.type_c[method] + 1})

    def top_10_size(self, line):
        mas = line.split()
        self.top_size.append({'ip': mas[0], 'time': mas[3][1:], 'method': mas[5][1:],
                              'url': mas[6], 'status': int(mas[8]), 'size': int(mas[9])})

    def top_10_client_size(self, line, status_code):
        mas = line.split()
        if mas[8][0] == status_code:
            self.top_client_size.append({'ip': mas[0], 'method': mas[5][1:], 'url': mas[6],
                                         'status': int(mas[8]), 'size': int(mas[9])})

    def top_10_client(self, line, status_code):
        mas = line.split()
        if mas[8][0] == status_code:
            if (mas[0], mas[5][1:], mas[6], int(mas[8])) not in self.top_client.keys():
                self.top_client.update({(mas[0], mas[5][1:], mas[6], int(mas[8])): 1})
            else:
                self.top_client[(mas[0], mas[5][1:], mas[6], int(mas[8]))] += 1

    def read(self, path):
        with open(path) as f:
            for line in f:
                self.total_count += 1
                self.type_count(line)
                self.top_10_size(line)
                self.top_10_client(line, '4')
                self.top_10_client_size(line, '4')
        self.top_size = [el for el, _ in groupby(sorted(self.top_size, key=lambda i: i['size'], reverse=True))]
        self.top_client = [{'ip': ip, 'method': method, 'url': url, 'status': status, 'count': count} for
                           (ip, method, url, status), count in
                           sorted(self.top_client.items(), key=lambda x: x[1], reverse=True)[:10]]
        self.top_client_size = [el for el, _ in groupby(sorted(self.top_client_size, key=lambda i: i['size'],
                                                               reverse=True))][:10]

    def read_file(self, path_dir_orm=None, file_orm=None):
        if file_orm is not None:
            self.read(f'{path_dir_orm}/{file_orm}')
        elif path_dir_orm is not None:
            for file in path_dir_orm:
                if file.endswith('.log'):
                    self.read(f'{path_dir_orm}/{file}')
        else:
            if args.filename is None:
                for file in os.listdir(args.dir):
                    if file.endswith('.log'):
                        self.read(f'{args.dir}/{file}')
            else:
                self.read(f'{args.dir}/{args.filename}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser_addoption(parser)
    args = parser.parse_args()
    a = Scripts()
    a.read_file()
    a.pack_to_file()
