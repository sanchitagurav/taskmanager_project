from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .models import Task
from .serializers import TaskSerializer, RegisterSerializer
from .permissions import IsOwnerOrAdmin

User = get_user_model()

# User Register
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# Task CRUD API
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            # admin can view all tasks
            return Task.objects.all().order_by('-created_at')
        # normal user sees only own tasks
        return Task.objects.filter(owner=user).order_by('-created_at')

    def perform_create(self, serializer):
        # while creating task → assign logged in user as owner
        serializer.save(owner=self.request.user)
