from celery import shared_task
from .service import request


@shared_task
def execution(pk):
    request(pk)
