import pytest


class TestLinux:

    @pytest.mark.LINUX
    def test_root(self, linux_client):
        root = linux_client.exec_root_cmd('whoami')
        assert 'root' == root[:-1]

        messages = linux_client.exec_root_cmd('tail /var/log/messages')
        assert len(messages)

    @pytest.mark.LINUX
    def test_connect(self, linux_client):

        # Check activity of http port for nginx
        check = linux_client.exec_root_cmd('firewall-cmd --list-all')
        if f'{linux_client.kwargs["http_port"]}/tcp' not in check:
            # Enable nginx work with http
            commands_http_enable = [
                'firewall-cmd --permanent --zone=public --add-port=8080/tcp',
                'firewall-cmd --reload',
                'systemctl restart nginx'
            ]
            for c in commands_http_enable:
                linux_client.exec_root_cmd(c)

        http = linux_client.test_port_nginx()
        assert 200 == http.status_code

        # Check nginx work via server side
        nginx = linux_client.exec_root_cmd('netstat -ltpn | grep nginx')
        assert 'tcp' and 'LISTEN' and 'nginx' in nginx

    @pytest.mark.LINUX
    def test_nginx_without_working_nginx(self, linux_client):

        # Disable nginx work with http
        commands_http_disable = [
            'firewall-cmd --permanent --zone=public --remove-port=8080/tcp',
            'firewall-cmd --reload',
            'systemctl restart nginx'
        ]
        for c in commands_http_disable:
            linux_client.exec_root_cmd(c)

        http = linux_client.test_port_nginx()
        assert http == 'Error'

        # Check nginx work via server side
        nginx = linux_client.exec_root_cmd('netstat -ltpn | grep nginx')
        assert 'tcp' and 'LISTEN' and 'nginx' in nginx
