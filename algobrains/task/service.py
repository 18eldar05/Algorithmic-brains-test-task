import json
import time
import httpx
from .models import *
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")

logging.info("Start of service.py")


def make_httpx_request(pk):
    logging.info("!!!make_httpx_request!!!")
    try:
        instance = Task.objects.get(pk=pk)
    except Task.DoesNotExist as err:
        logging.error("No Task found:", err)

    instance.status = "in_process"
    instance.save()
    time.sleep(3)

    method = instance.method
    url = instance.url
    headers = json.loads(instance.headers_from_client)
    body = json.loads(instance.body_from_client)

    response = httpx.request(method, url, headers=headers, json=body)

    instance.http_status_code = response.status_code
    resp_body = response.json()
    instance.body_from_service = json.dumps(resp_body)
    instance.length = response.headers.get('content-length', 0)
    if response.is_error:
        instance.status = "error"
    else:
        instance.status = "done"
    instance.save()
