# Content

## Bash

Appropriate readme in `bash` dir, has python and bash scripts for 1st task.

## Linux

Consists of a `SSH` Class with functions `test_port_nginx` and `exec_root_cmd`.
`exec_root_cmd` afford you to run command under root.
`test_port_nginx` afford you to test nginx via http.

## Mock

It is a mock server with 2 endpoints `/users` for doing `post` and `/users/{id}` for collecting `GET` methods.

## ORM

`models.py` consists of table descriptors for database.
`go_log.py` consists of some functions for insertion data from python script from `bash` directory in database.
`create_db.py` afford you to create database, if it not exists, and create tables from `models`.

## Socket_client

Consists of a `MySocket` Class with functions for getting, posting and receive data without `requests` library.

## Conftest.py

`host` and `port` params for `mock` server and `socket`.
`linux_host`, `linux_port` to connect to VirtualMachine via ssh.
`http_port` is an nginx port on VirtualMachine.
`username` and `password` are login and password for VirtualMachine (password must be the same for superuser).
`db_name` is a name of a database.
`db_login`, `db_host` and `db_password` parameters to connect to maraidb.
`path_dir_orm` is a path to directory where your `.log` are located.
`file_orm` is a filename if you want to use only specific file.




