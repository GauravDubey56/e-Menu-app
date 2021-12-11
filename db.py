import pymysql
import os
from flask import json, jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection = os.environ.get('CLOUD_SQL_CONN_NAME')

def open_conn():
     unix_socket = '/cloudsql/{}'.format(db_connection)
     print(db_user)
     print(db_name)
     print(db_connection)
     try:
          if os.environ.get('GAE_ENV') == 'standard':
               conn = pymysql.connect(user = db_user,
                                   password = db_password,
                                   unix_socket = unix_socket,
                                   db = db_name,
                                   cursorclass = pymysql.cursors.DictCursor
                                   )
               print(conn)
               return conn
     except pymysql.MySQLError as e:
          print(e)
          return e
     

def get():
     conn = open_conn()
     with conn.cursor() as cursor:
          res = cursor.execute('SELECT * FROM test')
          data = cursor.fetchall()
          if res > 0:
               resData = jsonify(data)
          else:
               resData = 'No data found'
          return resData

def create(data):
     conn = open_conn()
     with conn.cursor() as cursor:
          cursor.execute('INSERT INTO test (id, name, catg) VALUES(%s, %s, %s)', (data["id"], data["name"], data["catg"]))
     conn.commit()
     conn.close()