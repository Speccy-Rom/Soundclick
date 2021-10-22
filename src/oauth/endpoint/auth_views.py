from django.shortcuts import render


def login_google(request):
    """Вход через google
    """
    context = {}
    return render(request, 'oauth/google_login.html', context)
