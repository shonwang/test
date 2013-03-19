#__author__ = 'shon'

import sqlalchemy
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class user(Base):
    __tablename__='user'

    id=Column(Integer,primary_key=True)
    name=Column(String)
    fullname=Column(String)
    password=Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.name,self.fullname,self.password)

class database(object):
    def __init__(self):
        self.database_engine = create_engine('sqlite:///:memory:',echo=True)
        self.Session = sessionmaker(bind=self.database_engine)
        self.session = self.Session()
        Base.metadata.create_all(self.database_engine)

    def insert(self, name, fullname, password):
        tmp = user(name, fullname, password)
        self.session.add(tmp)
        self.session.commit()

if __name__ == '__main__':
    my_database = database()
    my_database.insert('jet','jet wei','123')
    my_database.insert('tom','tom geng','123')