import os

from dotenv import load_dotenv

load_dotenv()

BATCH_SIZE = 1000
UPDATE_TIME = 10

POSTGRES_DSN = {
    'dbname': os.environ.get('POSTGRES_DB'),
    'user': os.environ.get('POSTGRES_USER'),
    'password': os.environ.get('POSTGRES_PASSWORD'),
    'host': os.environ.get('DB_HOST', 'localhost'),
    'port': os.environ.get('DB_PORT', 5432),
    'options': '-c search_path=content'
}

ELASTIC_DSN = {
    'hosts': ['http://{}:{}'.format(os.environ.get('ELASTIC_HOST'),
                                    os.environ.get('ELASTIC_PORT'))],
    'basic_auth': (
        os.environ.get('ELASTIC_USER'),
        os.environ.get('ELASTIC_PASSWORD')
    )
}

REDIS_DSL = {
    'host': os.environ.get('REDIS_HOST'),
    'port': os.environ.get('REDIS_PORT'),
    'decode_responses': True
}

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
