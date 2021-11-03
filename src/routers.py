from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="SoundClick",
        default_version="v1",
        description="Soundclick is a music platform whose functionality is very similar "
        "to Soundcloud. The musical component is quite diverse.",
        terms_of_service="https://github.com/Speccy-Rom/Soundclick",
        contact=openapi.Contact(email="speccy@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("auth/", include("src.oauth.urls")),
]
