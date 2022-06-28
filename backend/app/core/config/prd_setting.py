import os

from typing import Union, Optional

from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress


class Settings(BaseSettings):
    # 生产模式配置
    VERSION: str = "0.0.1"
    DEBUG: bool = False
    # 项目文档
    TITLE: str = "lpr-server"
    DESCRIPTION: str = "lpr-server"

    # 文档地址 生产环境关闭 None
    DOCS_URL: Optional[str] = None
    # 文档关联请求数据接口 生产环境关闭 None
    OPENAPI_URL: Optional[str] = None
    # 生产环境关闭 redoc 文档
    REDOC_URL: Optional[str] = None
    REDOC_TAG = [
        {
            "name": "lprAPI",
            "description": "lpr-server",
        },
    ]

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    ALGORITHM = "HS256"

    # 生产环境保管好 SECRET_KEY
    SECRET_KEY: str = os.getenv("SECRET_KEY")

    # 生产环境项目根路径
    BASE_PATH: str = "/server"

    # MySql配置
    MYSQL_USERNAME: str = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD", "admin")
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = os.getenv("MYSQL_HOST", "127.0.0.1")
    MYSQL_DATABASE: str = os.getenv("MYSQL_DB", "xxx")

    # MySql地址
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@" \
                              f"{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"

    # redis配置
    REDIS_HOST: str = "127.0.0.1"
    REDIS_PASSWORD: str = ""
    REDIS_DB: int = 0
    REDIS_PORT: int = 6379
    REDIS_URL: str = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}?encoding=utf-8"
    REDIS_TIMEOUT: int = 5  # redis连接超时时间

    # CASBIN_MODEL_PATH: str = "./resource/rbac_model.conf"




settings = Settings()
