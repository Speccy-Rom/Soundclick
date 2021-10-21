from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """построение пути к файлу."""
    return f"avatar/{instance.id}/{file}"


def validate_size_image(file_obj):
    """Проверка размера файла."""
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла {megabyte_limit}MB")
