import threading

from flask import Flask, request, abort

app = Flask(__name__)

users = {'Akkakiy13': 0, 'Test': 1}


def run_mock(host, port):
    server = threading.Thread(target=app.run, kwargs={'host': host, 'port': port})
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/vk_id', methods=['POST'])
def create_user():
    user = request.form['user']
    users.update({user: len(users)})


@app.route('/vk_id/<username>')
def get_vk_id(username: str):
    user_id = users.get(username)
    if user_id is not None:
        return {'vk_id': user_id}, 200
    else:
        abort(404)


@app.route('/shutdown')
def shutdown():
    shutdown_mock()


if __name__ == '__main__':
    run_mock('0.0.0.0', 5000)
