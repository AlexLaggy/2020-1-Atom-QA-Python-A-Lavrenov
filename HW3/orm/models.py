from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class Size(Base):
    __tablename__ = 'size'
    id = Column(Integer, primary_key=True)
    ip = Column(String(200))
    method = Column(String(7))
    url = Column(String(200))
    time = Column(String(30))
    size = Column(String(200))

    def __init__(self, ip, method, url, time, size):
        self.ip = ip
        self.method = method
        self.url = url
        self.time = time
        self.size = size


class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    ip = Column(String(200))
    method = Column(String(7))
    url = Column(String(200))
    status_code = Column(Integer)

    def __init__(self, ip, method, url, status_code):
        self.ip = ip
        self.method = method
        self.url = url
        self.status_code = status_code


class Server(Base):
    __tablename__ = 'server'
    id = Column(Integer, primary_key=True)
    ip = Column(String(200))
    method = Column(String(7))
    url = Column(String(200))
    status_code = Column(Integer)

    def __init__(self, ip, method, url, status_code):
        self.ip = ip
        self.method = method
        self.url = url
        self.status_code = status_code
