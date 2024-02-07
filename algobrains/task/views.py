from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import TaskSerializerPost, TaskSerializerGet
from .tasks import execution


class TaskAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        try:
            instance = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404("No Task found!")

        return Response({
            'Response': TaskSerializerGet(instance).data
        }, status=200)

    def post(self, request):
        serializer = TaskSerializerPost(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.create(serializer.validated_data)

        execution.delay(instance.pk)

        return Response({'id': instance.pk}, status=200)
