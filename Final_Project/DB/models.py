from sqlalchemy import Column, Integer, String, SmallInteger, UniqueConstraint, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TestUsers(Base):
    __tablename__ = 'test_users'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    username = Column(String(16), nullable=True)
    password = Column(String(255), nullable=False)
    email = Column(String(64), nullable=False)
    access = Column(SmallInteger, nullable=True)
    active = Column(SmallInteger, nullable=True)
    start_active_time = Column(DateTime, nullable=True)
    UniqueConstraint('email', name='email')
    UniqueConstraint('username', name='ix_test_users_username')

    def __repr__(self):
        return f"<test_users(" \
               f"id='{self.id}'," \
               f"username='{self.username}'," \
               f"password='{self.password}'," \
               f"email='{self.email}'," \
               f"access='{self.access}'," \
               f"active='{self.active}'," \
               f"start_active_time='{self.start_active_time}')>"
