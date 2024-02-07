import json

from rest_framework import serializers
from .models import *


class TaskSerializerGet(serializers.Serializer):
    id = serializers.IntegerField()
    status = serializers.CharField(max_length=10)
    http_status_code = serializers.IntegerField()
    body_from_service = serializers.CharField()
    length = serializers.IntegerField()
    method = serializers.CharField(max_length=6)
    url = serializers.CharField(max_length=500)
    headers_from_client = serializers.CharField()
    body_from_client = serializers.CharField()
    time_create = serializers.DateTimeField()
    time_update = serializers.DateTimeField()


class TaskSerializerPost(serializers.Serializer):
    method = serializers.CharField(max_length=6)
    url = serializers.CharField(max_length=500)
    headers_from_client = serializers.DictField()
    body_from_client = serializers.DictField()

    def create(self, validated_data):
        return Task.objects.create(
            method=validated_data["method"],
            url=validated_data["url"],
            headers_from_client=json.dumps(validated_data["headers_from_client"]),
            body_from_client=json.dumps(validated_data["body_from_client"]),
        )
