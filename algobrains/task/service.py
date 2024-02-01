import time
import httpx
from django.http import Http404
from .models import Task


def request(pk):
    try:
        instance = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        raise Http404("No Task found!")

    instance.status = "in_process"
    instance.save()

    time.sleep(8)

    method = instance.method
    url = instance.url
    headers = eval(instance.headers_from_client)

    if method == "GET":
        response = httpx.get(url, headers=headers)
    elif method == "POST":
        response = httpx.post(url, json=headers)
    else:
        instance.status = "error"
        instance.save()
        raise Exception("Error: unknown method")

    instance.http_status_code = response.status_code
    instance.headers_from_service = response.headers
    instance.length = response.headers.get('content-length', 0)
    instance.status = "done"
    instance.save()
