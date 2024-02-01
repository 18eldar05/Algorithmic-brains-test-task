from django.urls import reverse
from .models import Task
from rest_framework.test import APITestCase


class Test(APITestCase):
    def setUp(self):
        self.instance = Task.objects.create(method="GET", url="https://httpbin.org/get", headers_from_client="{'key7': 'value7', 'key8': 'value8'}")

    def test_get_none(self):
        response = self.client.get(reverse("task_none"))
        self.assertEqual(response.status_code, 404)

    def test_get(self):
        response = self.client.get(reverse("task_pk", kwargs={"pk": self.instance.pk}))
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        self.data = {
            "method": "GET",
            "url": "https://httpbin.org/get",
            "headers_from_client":  "{'key7': 'value7', 'key8': 'value8'}"
        }

        response = self.client.post(reverse("task_none"), self.data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json().get('id'), int)
