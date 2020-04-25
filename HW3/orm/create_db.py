from sqlalchemy import create_engine
from orm.models import Base

engine = create_engine('mysql+pymysql://admin:password@localhost/bash', echo=True)
# conn = engine.connect()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
# conn.execute('commit')
# conn.execute('create database bash')
# conn.close()
