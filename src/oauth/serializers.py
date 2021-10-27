from rest_framework import serializers

from src.oauth import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthUser
        fields = ('avatar', 'country', 'city', 'bio', 'display_name', 'email')


class GoogleAuthSerializer(serializers.Serializer):
    """сериализация данных от google
    """
    email = serializers.EmailField()
    token = serializers.CharField()
