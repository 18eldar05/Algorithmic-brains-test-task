from django.db import models


class Task(models.Model):
    status = models.CharField(default="new", max_length=255)
    http_status_code = models.IntegerField(default=0)
    headers_from_service = models.TextField(default="")
    length = models.IntegerField(default=0)
    method = models.CharField(blank=True,  max_length=8, choices=[("GET", "GET"), ("POST", "POST"), ])
    url = models.CharField(blank=True, max_length=500)
    headers_from_client = models.TextField(blank=True)
