from rest_framework import serializers


class GoogleAuthSerializer(serializers.Serializer):
    """сериализация данных от google
    """
    email = serializers.EmailField()
    token = serializers.CharField()
