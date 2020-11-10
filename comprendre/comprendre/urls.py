"""
Comprendre URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from comprendre.meetings.v1.urls import comp_router_v1


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version=settings.REST_FRAMEWORK['DEFAULT_VERSION'],
      description="Documantation for the comprendre app API.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@comp.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Swagger urls : https://github.com/axnsan12/drf-yasg
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    url(r'^v1/', include((comp_router_v1.urls, 'v1'), namespace='v1')),
]
