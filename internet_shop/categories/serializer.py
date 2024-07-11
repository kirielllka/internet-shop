from .models import Categories

from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category_name = serializers.CharField(max_length=100)
    

    def create(self, validated_data):
        return Categories(**validated_data)


    def update(self, instance, validated_data):
        instance.category_name = validated_data.get('category_name', instance.category_name)
        
        return instance