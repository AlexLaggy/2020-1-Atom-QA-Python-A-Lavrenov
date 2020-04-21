import pytest


class TestApi:
    segment_id = None

    @pytest.mark.API
    def test_create_segment(self, api_client):
        segment_name = 'Test_Api'
        segment = api_client.create_segment(segment_name)

        response, location = api_client.check_segment(segment.json().get('id'))
        assert response.url == location and response.status_code == 200

    @pytest.mark.API
    def test_delete_segment(self, api_client):
        segment_name = 'Test_Api_Deleted'
        segment = api_client.create_segment(segment_name)
        segment_id = segment.json().get('id')

        response = api_client.delete_segment(segment_id)
        assert response.status_code == 204
