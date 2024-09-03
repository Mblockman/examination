import os

BASE_DIR = os.path.dirname(__file__)

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'db': 'examination',
    'charset': 'utf8mb4'
}

SECRET_KEY = "dev"