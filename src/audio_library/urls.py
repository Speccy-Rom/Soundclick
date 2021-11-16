from django.urls import path

from . import views

urlpatterns = [
    path("genre/", views.GenreView.as_view()),

    path("license/", views.LicenseView.as_view({'get': 'list', 'post': 'create'})),
    path("license/<int:pk>/", views.LicenseView.as_view({'put': 'update', 'delete': 'destroy'})),

    path("album/", views.AlbumViews.as_view({'get': 'list', 'post': 'create'})),
    path("album/<int:pk>/", views.AlbumViews.as_view({'put': 'update', 'delete': 'destroy'})),

    path('author-album/<int:pk>/', views.PublicAlbumViews.as_view()),

]
