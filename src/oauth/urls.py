from django.urls import path

from .endpoint import views, auth_views

urlpatterns = [
    path('me/', views.UserView.as_view({'get': 'retrieve', 'put': 'update'})),

    path("google/", auth_views.google_auth),
    path("spotify-callback/", auth_views.spotify_auth),
    path("spotify-login/", auth_views.spotify_login),
    path("", auth_views.google_login),
]
