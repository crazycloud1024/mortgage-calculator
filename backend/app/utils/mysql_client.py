import pymysql
from dbutils.pooled_db import PooledDB
from core.config import settings


class MysqlUtil(object):
    # 连接池对象
    __pool = None

    def __init__(self):
        # 数据库构造函数，从连接池中取出连接，并生成操作游标
        self.pool = MysqlUtil.__get_conn()

    @staticmethod
    def __get_conn():
        """
        @summary: 静态方法，从连接池中取出连接
        @return MySQLdb.connection
        """
        host = settings.ZT_RDS_HOST
        username = settings.ZT_RDS_USER
        db_pwd = settings.ZT_RDS_PASSWD
        port = settings.ZT_RDS_PORT
        db_database = "zentao"
        if MysqlUtil.__pool is None:
            __pool = PooledDB(pymysql, mincached=1, maxcached=10, maxconnections=10,
                              host=host, port=port, user=username, passwd=db_pwd,
                              db=db_database, use_unicode=False, blocking=False, charset="utf8")
        return __pool

    def get_all(self, sql, *args, **kwargs):
        """
        @summary: 执行查询，并取出所有结果集
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list(字典对象)/boolean 查询到的结果集
        """
        try:
            con = self.pool.connection()
            cur = con.cursor()
            count = cur.execute(sql, *args, **kwargs)
            if count > 0:
                result = cur.fetchall()
            else:
                result = False
            return result
        except Exception as e:
            print('SQL执行有误,原因:', e)
        finally:
            cur.close()
            con.close()

    def execute(self, sql, *args, **kwargs):
        try:
            con = self.pool.connection()
            cur = con.cursor()
            cur.execute(sql, *args, **kwargs)
            con.commit()
        except Exception as e:
            con.rollback()  # 事务回滚
            print('SQL执行有误,原因:', e)
        finally:
            cur.close()
            con.close()
