import os
import redis
from werkzeug.utils import import_string

class Config(object):
    REDIS_HOST = os.environ.get("REDIS_HOST", "127.0.0.1")
    REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", None)
    SECRET_KEY = os.environ.get("SECRET_KEY", "Optional default value")
    SESSION_TYPE = "redis"
    redis_client = redis.StrictRedis(
        host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True
    )
    SESSION_REDIS = redis_client

class ConfigDev(Config):
    pass

class ConfigProd(Config):
    pass

def get_config() -> Config:
    return import_string(os.environ.get("CHAT_CONFIG", "chat.config.ConfigDev"))()
