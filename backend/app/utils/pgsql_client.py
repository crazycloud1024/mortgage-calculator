from contextlib import contextmanager
from threading import Semaphore
import psycopg2
from psycopg2 import pool
from app.core.config import settings

pgsql_config = {
    "host": settings.PG_HOST,
    "port": settings.PG_PORT,
    "database": settings.PG_DATABASE,
    "user": settings.PG_USER,
    "password": settings.PG_PASSWORD
}


class ReallyThreadedConnectionPool(psycopg2.pool.ThreadedConnectionPool):
    def __init__(self, minconn, maxconn, *args, **kwargs):
        self._semaphore = Semaphore(maxconn)
        super().__init__(minconn, maxconn, *args, **kwargs)

    def getconn(self, key=None):
        self._semaphore.acquire()
        return super().getconn(key)

    def putconn(self, *args, **kwargs):
        super().putconn(*args, **kwargs)
        self._semaphore.release()


cnxpool = ReallyThreadedConnectionPool(5, 10, **pgsql_config)


@contextmanager
def get_cursor():
    try:
        con = cnxpool.getconn()
        cursor = con.cursor()
        yield cursor
    except psycopg2.Error as e:
        print(e)
    finally:
        con.commit()
        cursor.close()
        cnxpool.putconn(con)


class PyPgsql(object):

    @staticmethod
    def get_all(*args, **kwargs):
        with get_cursor() as cursor:
            cursor.execute(*args, **kwargs)
            return cursor.fetchall()


if __name__ == '__main__':
    pass
