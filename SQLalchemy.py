#__author__ = 'shon'
import sqlalchemy
from sqlalchemy import *
import datetime
import os

print sqlalchemy.__version__

metatdata = MetaData('sqlite:///test_sqlite')

user_table = Table(
    'table_name_user', metatdata,
    Column('id', Integer, primary_key=True),
    Column('user_name', Unicode(16), unique=True, nullable=False),
    Column('password', Unicode(40), nullable=False),
    Column('display_name', Unicode(255), default=''),
    Column('created', DateTime,default=datetime.datetime.now())
)

group_table = Table(
    'table_name_group', metatdata,
    Column('id', Integer, primary_key='True'),
    Column('group_name', Unicode(16), unique=True, nullable=False)
)

permission_table = Table(
    'table_name_permission', metatdata,
    Column('id', Integer, primary_key= True),
    Column('permission_name', Unicode(16), unique=True, nullable=False)
)

user_group_table = Table(
    'table_name_user_group', metatdata,
    Column('user_id', None, ForeignKey('table_name_user.id'), primary_key=True),
    Column('group_id', None, ForeignKey('table_name_group.id'), primary_key=True),
)

group_permission_table = Table(
    'table_name_group_permission', metatdata,
    Column('permission_id', None, ForeignKey('table_name_permission.id'), primary_key=True),
    Column('group_id', None, ForeignKey('table_name_group.id'), primary_key=True)
)

metatdata.create_all()
metatdata.bind.echo = True

stmt = user_table.insert()
stmt.execute(user_name='rick', password='123', display_name = 'Rick Copeland Clone')
stmt.execute(user_name='zong', password='123', display_name = 'Zong Chuanyi')
metatdata.bind.echo = False

stmt = user_table.select()
result = stmt.execute()
#for row in result:
#    print row
#row = result.fetchone()
#print row.password
#print row['user_name']

