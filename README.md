HTTP server for a service that would make http requests to 3rd-party services

Commands:
docker-compose up
algobrains$ python3 manage.py runserver
algobrains$ celery -A algobrains worker -l info

POST:
http://127.0.0.1:8000/task/
{
    "method": "POST",
    "url": "https://httpbin.org/post",
    "headers_from_client":  "{'key88': 'value88', 'key99': 'value99'}"
}

GET:
http://127.0.0.1:8000/task/1/
