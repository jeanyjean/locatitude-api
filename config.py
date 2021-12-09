from decouple import config

OPENAPI_AUTOGEN_DIR = 'autogen'
DB_HOST = config('DB_HOST')
DB_USER = config('DB_USER')
DB_PASSWD = config('DB_PASSWORD')
DB_NAME = config('DB_NAME')

