import redis
from contextlib import contextmanager
from app.core.config import settings


def get_pool(host, port) -> redis.ConnectionPool:
    pool = redis.ConnectionPool(host=host, port=port, decode_responses=True, max_connections=100)
    return pool


redis_pool = get_pool(host=settings.REDIS_HOST, port=settings.REDIS_PORT)


@contextmanager
def get_redis_conn():
    try:
        redis_conn = redis.Redis(connection_pool=redis_pool)
        yield redis_conn
    except:
        redis_conn.close()
    finally:
        redis_conn.close()


if __name__ == '__main__':
    with get_redis_conn() as conn:
        conn.set("a", "123", ex=4)
