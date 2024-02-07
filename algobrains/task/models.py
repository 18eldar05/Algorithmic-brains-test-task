from django.db import models
from django.urls import reverse


class Task(models.Model):
    class ChoiceMethod(models.TextChoices):
        GET = "GET",
        POST = "POST"
        PUT = "PUT",
        PATCH = "PATCH"
        DELETE = "DELETE"

    class ChoiceStatus(models.TextChoices):
        new = "new",
        in_process = "in_process",
        error = "error",
        done = "done"

    status = models.CharField(max_length=10, choices=ChoiceStatus.choices, default=ChoiceStatus.new)
    http_status_code = models.IntegerField(default=0)
    body_from_service = models.TextField(default="")
    length = models.IntegerField(default=0)
    method = models.CharField(max_length=6, choices=ChoiceMethod.choices, default=ChoiceMethod.GET)
    url = models.CharField(blank=True, max_length=500)
    headers_from_client = models.TextField(blank=True)
    body_from_client = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('task_pk', kwargs={'pk': self.pk})
