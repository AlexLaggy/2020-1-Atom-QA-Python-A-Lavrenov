from mock.mock import users


def add_user(user_id: int, user_data: dict):
    users.update({str(user_id): user_data})


def test_valid_get(mock_server, socket_client):
    user = {'name': 'Ilya', 'surname': 'Kirillov'}
    add_user(1, user)

    socket_client.run()
    socket_client.get_request('/users/1')
    result = socket_client.receive()
    assert result['data'] == user


def test_invalid_get(mock_server, socket_client):
    user = {'name': 'Yaroslav', 'surname': 'Cherednichenko'}
    add_user(2, user)

    socket_client.run()
    socket_client.get_request('/users/3')
    result = socket_client.receive()
    assert result['status_code'] == 404


def test_valid_post(mock_server, socket_client):
    info = {'name': 'ALex', 'surname': 'Laggy'}
    socket_client.run()
    socket_client.post_request('/users', info)
    result = socket_client.receive()
    assert result['status_code'] == 200  # 201, but can't check result
    assert result['data'] == info
