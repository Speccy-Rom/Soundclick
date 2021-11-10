from rest_framework import parsers, permissions, viewsets

from src.base.permissions import IsAuthor
from src.oauth import models, serializers


class UserView(viewsets.ModelViewSet):
    """Просмотр и редактирование данных пользователя."""

    parser_classes = (parsers.MultiPartParser,)
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user

    def get_object(self):
        return self.get_queryset()


class AuthorsView(viewsets.ReadOnlyModelViewSet):
    """Вывод списка авторов"""

    queryset = models.AuthUser.objects.all().prefetch_related("social_link")
    serializer_class = serializers.AuthorSerializer


class SocialLinkView(viewsets.ModelViewSet):
    """CRUD ссылок соц. сетей пользователя"""

    serializer_class = serializers.SocialLinkSerializer
    permissions_classes = [IsAuthor]

    def get_queryset(self):
        return self.request.user.social_link.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
