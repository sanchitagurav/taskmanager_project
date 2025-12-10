from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task

User = get_user_model()

# User Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

# Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at', 'owner']
