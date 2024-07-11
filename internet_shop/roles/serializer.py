from .models import Roles

from rest_framework import serializers


class RolesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    role_name = serializers.CharField(max_length=100)


    def create(self, validated_data):
        return Roles(**validated_data)

    def update(self, instance, validated_data):
        instance.role_name = validated_data.get('role_name', instance.role_name)
        return instance