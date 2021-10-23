from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from .. import serializers
from ..services.google import check_google_auth


def google_login(request):
    """Вход через Google
    """
    context = {}
    return render(request, 'oauth/google_login.html', context)


@api_view(['POST'])
def google_auth(request):
    """Подтверждение авторизации через Google
    """
    google_data = serializers.GoogleAuthSerializer(data=request.data)
    if google_data.is_valid():
        token = check_google_auth(google_data.data)
        return Response(token)
    else:
        return AuthenticationFailed(code=403, detail='Bad data Google')
