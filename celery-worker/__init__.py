import logging
from celery import Celery

BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

app = Celery('test', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)


logger = logging.getLogger('hello')


@app.task(name='test_hello', serializer='json')
def test_hello(a, b, c):
    logger.info('hello')
    return [a, b, c]
