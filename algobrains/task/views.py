from django.http import Http404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializerPost, TaskSerializerGet
from .tasks import execution


class TaskAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            instance = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404("No Task found!")

        return Response({
            'Response': TaskSerializerGet(instance).data
        }, status=200)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = TaskSerializerPost(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        execution.delay(instance.pk)

        return Response({'id': instance.pk}, status=200)
