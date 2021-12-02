from django.contrib import admin

from .models import Album, Comment, Genre, License, Playlist, Track


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    list_display_links = ("user",)
    list_filter = ("user",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)
    search_fields = ("name",)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name")
    list_display_links = ("user",)
    list_filter = ("user", "private")
    search_fields = ("name",)


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "title",
        "created_at",
    )
    list_display_links = ("user",)
    list_filter = ("genre", "album", "created_at")
    search_fields = ("user", "genre__name")
    raw_id_fields = ("genre",)
    date_hierarchy = "created_at"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "track")
    list_display_links = ("user",)
    list_filter = ("user", "track", "created_at")
    date_hierarchy = "created_at"


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title")
    list_display_links = ("user",)
    search_fields = ("user", "tracks__title")
    list_filter = ("user",)
    raw_id_fields = ("tracks",)
