from celery import shared_task
from .service import make_httpx_request


@shared_task
def execution(pk):
    make_httpx_request(pk)
