from rest_framework import serializers

from rest_framework.serializers import Serializer
from .models import StudentModel


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return StudentModel.objects.create(**validated_data)
