from .models import Users
from database import session_maker

import hashlib
import jwt
import datetime

from rest_framework import serializers
from rest_framework.response import Response

from .dependencies import hashing
class RegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)
    role = serializers.IntegerField(default=3, read_only=True)

    def verify_email(self,value) -> str:
        session = session_maker()
        if session.query(Users).filter_by(email=value).first():
            session.close()
            raise serializers.ValidationError("Данный email уже существует")
        session.close()
        return value

    def create(self, validated_data):
        session = session_maker()
        email = self.verify_email(validated_data["email"])
        password = validated_data["password"]
        hashed_password = hashing(password)
        user = Users(email=email, hashed_password=hashed_password, role=3)
        session.add(user)
        session.commit()
        session.close()
        return user



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)

    def validate(self, validated_data):
        session = session_maker()
        email = validated_data["email"]
        password = validated_data["password"]
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        user = session.query(Users).filter_by(email=email, hashed_password=hashed_password).first()
        session.close()
        if not user:
            raise serializers.ValidationError("Неверные данные для входа")
        return validated_data


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    hashed_password = serializers.CharField()
    role = serializers.IntegerField()

    def create(self, validated_data):
        return Users(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.hashed_password = validated_data.get('hashed_password', instance.hashed_password)
        instance.role = validated_data.get('role', instance.role)
        return instance

class UsersPasswordUpdateSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    hashed_password = serializers.CharField()

