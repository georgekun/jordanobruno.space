from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Документация",
        default_version='v1',),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/form/', include("formapp.urls")), 
    path('api/personal/', include("personalvaultapp.urls")),
    path('api/projects/', include("projectsapp.urls")),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
