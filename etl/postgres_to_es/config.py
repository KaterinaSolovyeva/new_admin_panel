from pydantic import BaseSettings, Field


class PostgresSettings(BaseSettings):
    dbname: str = Field('movies_database', env='POSTGRES_DB')
    user: str = Field('app', env='POSTGRES_USER')
    password: str = Field('123qwe', env='POSTGRES_PASSWORD')
    host: str = Field('localhost', env='DB_HOST')
    port: str = Field(5432, env='DB_PORT')
    options: str = '-c search_path=content'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class ElasticSettings(BaseSettings):
    hosts: str = Field('http://localhost:9200', env='ELASTIC_ADDRESS')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class RedisSettings(BaseSettings):
    host: str = Field('redis', env='REDIS_HOST')
    port: str = Field('6379', env='REDIS_PORT')
    decode_responses: bool = True

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class Settings(BaseSettings):
    BATCH_SIZE: int = 100
    UPDATE_TIME: int = 10
    POSTGRES_DSN: PostgresSettings = PostgresSettings()
    ELASTIC_DSN: ElasticSettings = ElasticSettings()
    REDIS_DSN: RedisSettings = RedisSettings()


LOGGING_CONFIG = {
    'version': 1,
    'root': {
        "handlers": ['default', 'file'],
        "level": 'INFO'
    },
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] %(levelname)s - %(message)s [%(pathname)s.%(funcName)s:%(lineno)d]', # noqa
            'datefmt': '%d/%m/%Y %H:%M:%S',
        },
    },
    'handlers': {
        'default': {
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': 'etl.log',
        }
    },
}
