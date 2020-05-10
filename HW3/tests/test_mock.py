import pytest


class TestMock:
    @pytest.mark.MOCK
    def test_valid_post(self, mock_server, socket_client):
        info = {'name': 'ALex', 'surname': 'Laggy'}
        socket_client.run()
        socket_client.post_request('/users', info)
        result = socket_client.receive()

        assert result['status_code'] == 200  # 201, but can't check result
        assert result['data'] == info

    @pytest.mark.MOCK
    def test_valid_get(self, mock_server, socket_client):
        user = {'name': 'Ilya', 'surname': 'Kirillov'}
        socket_client.run()
        socket_client.post_request('/users', user)
        socket_client.receive()

        socket_client.run()
        socket_client.get_request('/users/0')
        result = socket_client.receive()
        assert result['status_code'] == 200

    @pytest.mark.MOCK
    def test_invalid_get(self, mock_server, socket_client):
        user = {'name': 'Yaroslav', 'surname': 'Cherednichenko'}
        socket_client.run()
        socket_client.post_request('/users', user)
        socket_client.receive()

        socket_client.run()
        socket_client.get_request('/users/100')
        result = socket_client.receive()
        assert result['status_code'] == 404
