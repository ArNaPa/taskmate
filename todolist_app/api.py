from .models import Tasklist
from rest_framework import routers, serializers, viewsets, permissions


# Serializers define the API representation.
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasklist
        fields = ['id', 'task', 'manage', 'done']
        read_only_fields = ['id', ]


# ViewSets define the view behavior.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasklist.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer
