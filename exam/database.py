import pymysql
from config import DB_CONFIG

def get_db_connection():
    return pymysql.connect(**DB_CONFIG)

def execute_query(query, args=None):
    conn = get_db_connection()
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query, args or ())
            if query.strip().upper().startswith('SELECT'):
                return cursor.fetchall()
            conn.commit()
    finally:
        conn.close()