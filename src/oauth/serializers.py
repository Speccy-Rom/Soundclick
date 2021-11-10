from rest_framework import serializers

from src.oauth import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthUser
        fields = ("avatar", "country", "city", "bio", "display_name", "email")


class SocialLinkSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.SocialLink
        fields = ("id", "link")


class AuthorSerializer(serializers.ModelSerializer):
    social_link = SocialLinkSerializer(many=True)

    class Meta:
        model = models.AuthUser
        fields = (
            "id",
            "avatar",
            "country",
            "city",
            "bio",
            "display_name",
            "email",
            "social_link",
        )


class GoogleAuthSerializer(serializers.Serializer):
    """сериализация данных от google"""

    email = serializers.EmailField()
    token = serializers.CharField()
