import uuid
import os

DEBUG = False
TESTING = False
SECRET_KEY = str(uuid.uuid4())
USERNAME = str(uuid.uuid4())
PASSWORD = str(uuid.uuid4())

NAME = 'datapusher'

# database

SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s/%s' % (
    os.environ['CKAN_DATAPUSHER'],
    os.environ['CKAN_DATAPUSHER_PASS'],
    os.environ['DB_PORT_5432_TCP_ADDR'],
    os.environ['CKAN_DATAPUSHER_DB'],
)

# webserver host and port

HOST = '0.0.0.0'
PORT = 8800

# logging

#FROM_EMAIL = 'server-error@example.com'
#ADMINS = ['yourname@example.com']  # where to send emails

LOG_FILE = '/tmp/ckan_datapusher_service.log'
STDERR = True