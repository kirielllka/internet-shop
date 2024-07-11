from .models import Client

from rest_framework import serializers


class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Client(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        return instance

    def update(self, instance, validated_data):
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.category = validated_data.get('category', instance.category)
        instance.description = validated_data.get('description', instance.description)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.count_of_sells = validated_data.get('count_of_sells', instance.count_of_sells)
        instance.discount = validated_data.get('discount', instance.discount)
        return instance