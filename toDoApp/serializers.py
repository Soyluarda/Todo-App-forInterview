from rest_framework import serializers
from .models import toDo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = toDo
        fields = "__all__"