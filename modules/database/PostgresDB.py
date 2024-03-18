import psycopg2

from sensitive_settings import db_host, db_name, db_password, db_user


class PostgresDB:
    def __init__(self):
        self.conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host)
