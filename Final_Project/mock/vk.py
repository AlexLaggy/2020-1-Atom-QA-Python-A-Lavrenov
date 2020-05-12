import threading

from flask import Flask, request

app = Flask(__name__)
mas = {}


def run_mock(host, port):
    server = threading.Thread(target=app.run, kwargs={'host': host, 'port': port})
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/vk_id/<username>')
def get_vk_id(username: str):
    user = None
    for id, name in mas.items():
        if name == username:
            user = id
            break
    if user:
        return {'vk_id': user}, 200
    else:
        i = len(mas.keys())
        mas.update({i: username})
        return {'vk_id': i}, 201


@app.route('/shutdown')
def shutdown():
    shutdown_mock()


if __name__ == '__main__':
    run_mock('0.0.0.0', 5000)
