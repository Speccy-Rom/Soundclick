# Generated by Django 3.2.8 on 2021-10-17 09:43

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import src.base.services


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AuthUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=150, unique=True)),
                ("join_date", models.DateField(auto_now_add=True)),
                ("country", models.CharField(blank=True, max_length=30, null=True)),
                ("city", models.CharField(blank=True, max_length=30, null=True)),
                ("bio", models.TextField(blank=True, max_length=2000, null=True)),
                (
                    "display_name",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=src.base.services.get_path_upload_avatar,
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["jpg"]
                            ),
                            src.base.services.validate_size_image,
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SocialLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("link", models.URLField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="social_link",
                        to="oauth.authuser",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Follower",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subscriber",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscribers",
                        to="oauth.authuser",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owner",
                        to="oauth.authuser",
                    ),
                ),
            ],
        ),
    ]
