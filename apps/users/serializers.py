from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["created_at", "updated_at", "last_login"]

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "created_at", "updated_at", "last_login"]


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=120, min_length=6)
    password_confimation = serializers.CharField(max_length=120, min_length=6)

    def validate(self, data):
        if data["password"] != data["password_confimation"]:
            raise serializers.ValidationError(
                {"password": "Debe ingresar la misma contraseña"}
            )
        return data


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass
