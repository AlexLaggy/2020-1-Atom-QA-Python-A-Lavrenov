from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, SSHException

import requests


class SSH:
    def __init__(self, **kwargs):
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.kwargs = kwargs

    def __enter__(self):
        kw = self.kwargs
        try:
            self.client.connect(
                hostname=kw.get('hostname'),
                port=int(kw.get('port', 2222)),
                username=kw.get('username'),
                password=kw.get('password'),
            )
        except AuthenticationException:
            print("Authentication failed, please verify your credentials")
        except SSHException as sshException:
            print(f"Could not establish SSH connection {sshException}")

        """
        Возвращение self из метода означает,
        что метод возвращает ссылку на объект экземпляра, для которого он был вызван
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def exec_root_cmd(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(f"sudo -S -p '' {cmd}")
        stdin.write('centos\n')
        stdin.flush()

        data = stdout.read()
        data = data.decode()

        err = stderr.read()
        err = err.decode()
        if err:
            raise Exception(f'Err:{err}')
        return data

    def test_port_nginx(self):
        try:
            response = requests.get(f'http://{self.kwargs.get("hostname")}:{self.kwargs["http_port"]}')
        except IOError:
            response = 'Error'
        return response
