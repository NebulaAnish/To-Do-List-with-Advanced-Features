from rest_framework import serializers
from .models import ToDoItem

class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ['id', 'title','description','completed']

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

# class SaveFileSerializer(serializers.Serializer):
#     class Meta:
#         model = ToDoItem
#         fields = ['id', 'title','description','completed']