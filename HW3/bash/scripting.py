import argparse
import os
import json
from orm.go_log import add_to_client_table, add_to_server_table, add_to_size_table, session


def parser_addoption(parser):
    parser.add_argument('-d', '--dir', default='/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1]))
    parser.add_argument('-f', '--filename', default=None)
    parser.add_argument('-j', '--json', default=False, type=bool)


parser = argparse.ArgumentParser()
parser_addoption(parser)
args = parser.parse_args()

total_count = 0
type_c = {}
top_size = []
top_client = []
top_server = []


def pack_to_file(file='python_result.csv'):
    with open(file, 'w', newline='\n') as f:
        f.write(json.dumps(total_count))
        f.write(json.dumps(type_c))
        f.write(json.dumps(top_size))
        f.write(json.dumps(top_client))
        f.write(json.dumps(top_server))


def type_count(line):
    method = line.split()[5][1:]
    if method not in type_c.keys():
        type_c.update({method: 1})
    else:
        type_c.update({method: type_c[method] + 1})


def top_10_size(line):
    mas = line.split()
    top_size.append({'ip': mas[0], 'time': mas[3][1:], 'method': mas[5][1:],
                     'url': mas[6], 'status': int(mas[8]), 'size': int(mas[9])})


def top_10_client(line, status_code):
    mas = line.split()
    if status_code == '4':
        tt = top_client
    else:
        tt = top_server
    if mas[8][0] == status_code:
        # if mas[0] in top_client:
        #     if mas[5][1:] in top_client[mas[0]]:
        #         if mas[6] in top_client[mas[0]][mas[5][1:]]:
        #             if mas[8] in top_client[mas[0]][mas[5][1:]][mas[6]]:
        #                 top_client[mas[0]][mas[5][1:]][mas[6]][mas[8]]['count'] += 1
        #             else:
        #                 top_client[mas[0]][mas[5][1:]][mas[6]].update({mas[8]: {'count': 1}})
        #         else:
        #             top_client[mas[0]][mas[5][1:]].update({mas[6]: {mas[8]: {'count': 1}}})
        #     else:
        #         top_client[mas[0]].update({mas[5][1:]: {mas[6]: {mas[8]: {'count': 1}}}})
        # else:
        #     top_client.update({mas[0]: {mas[5][1:]: {mas[6]: {mas[8]: {'count': 1}}}}})
        # if dict(list(a[x].items())[0: 3])==dict(list(b[x].items())[0: 3])
        for d in tt:
            if {'ip': mas[0], 'method': mas[5][1:], 'url': mas[6], 'status': int(mas[8])} == dict(list(d.items())[0: 4]):
                d['count'] += 1
                return
        tt.append({'ip': mas[0], 'method': mas[5][1:], 'url': mas[6], 'status': int(mas[8]), 'count': 1})


def read_file():
    global total_count, top_size, top_client, top_server
    if args.filename is None:
        for file in os.listdir(args.dir):
            if file.endswith('.log'):
                with open(f'{args.dir}/{file}') as f:
                    for line in f:
                        total_count += 1
                        type_count(line)
                        top_10_size(line)
                        top_10_client(line, '4')
                        top_10_client(line, '5')
                top_size = sorted(top_size, key=lambda i: i['size'], reverse=True)[:10]
                top_client = sorted(top_client, key=lambda i: i['count'], reverse=True)[:10]
                top_server = sorted(top_server, key=lambda i: i['count'], reverse=True)[:10]


if __name__ == '__main__':
    read_file()
    pack_to_file()

    # Work with db
    add_to_size_table(top_size)
    add_to_client_table(top_client)
    add_to_server_table(top_server)
    session.commit()
    session.close()
