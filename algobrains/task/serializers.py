from rest_framework import serializers
from .models import Task


class TaskSerializerGet(serializers.Serializer):
    id = serializers.IntegerField()
    status = serializers.CharField(max_length=255)
    http_status_code = serializers.IntegerField()
    headers_from_service = serializers.CharField()
    length = serializers.IntegerField()
    method = serializers.CharField(max_length=8)
    url = serializers.CharField(max_length=500)
    headers_from_client = serializers.CharField()


class TaskSerializerPost(serializers.Serializer):
    method = serializers.CharField(max_length=8)
    url = serializers.CharField(max_length=500)
    headers_from_client = serializers.CharField()

    def create(self, validated_data):
        return Task.objects.create(**validated_data)
