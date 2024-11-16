from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(title="BobobAPI", default_version="v1",),public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("backend.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui",),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc",),
]