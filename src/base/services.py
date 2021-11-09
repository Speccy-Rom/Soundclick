from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """Построение пути к файлу format: (media)/avatar/user_id/photo.jpg."""
    return f"avatar/{instance.id}/{file}"


def get_path_upload_cover_album(instance, file):
    """Построение пути к файлу format: (media)/album/user_id/photo.jpg."""
    return f"album/user_{instance.id}/{file}"


def get_path_upload_track(instance, file):
    """Построение пути к файлу format: (media)/track/user_id/photo.jpg."""
    return f"track/user_{instance.id}/{file}"


def get_path_upload_playlist(instance, file):
    """Построение пути к файлу format: (media)/playlist/user_id/photo.jpg."""
    return f"playlist/{instance.id}/{file}"


def validate_size_image(file_obj):
    """Проверка размера файла."""
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла {megabyte_limit}MB")
