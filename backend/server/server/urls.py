from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Документация jordanobruno.space",
        default_version='v1',),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('back/admin/', admin.site.urls),

    path('back/api/form/', include("formapp.urls")), 
    path('back/api/personal/', include("personalvaultapp.urls")),
    path('back/api/projects/', include("projectsapp.urls")),

    path('back/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
