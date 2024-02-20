from django.urls import path

from .views import ApplicationView

urlpatterns = [
    path("application/new/", ApplicationView.as_view())    
]
