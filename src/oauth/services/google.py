from google.auth.transport import requests
from google.oauth2 import id_token
from rest_framework.exceptions import AuthenticationFailed

from src.oauth import serializers
from src.oauth.models import AuthUser
from . import base_auth


def check_google_auth(google_user: serializers.GoogleAuthSerializer):
    try:
        id_token.verify_oauth2_token(google_user['token'], requests.Request())
    except ValueError:
        return AuthenticationFailed(code=403, detail='Bad data Google')

    user, _ = AuthUser.objects.get_or_create(email=google_user['email'])
    return base_auth.create_token(user.id)
