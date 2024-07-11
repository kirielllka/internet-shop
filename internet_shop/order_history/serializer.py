from .models import OrderHistory

from rest_framework import serializers


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product = serializers.IntegerField()
    date = serializers.DateField()
    quantity = serializers.IntegerField()
    full_cost = serializers.FloatField()
    client = serializers.IntegerField()

    def create(self, validated_data):
        return OrderHistory(**validated_data)

    def update(self, instance, validated_data):
        instance.product = validated_data.get('product', instance.product)
        instance.date = validated_data.get('date', instance.date)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.full_cost = validated_data.get('full_coast', instance.full_cost)
        instance.client = validated_data.get('client', instance.client)
        return instance