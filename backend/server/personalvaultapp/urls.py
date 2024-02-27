from django.urls import path

from .views import (LatestProfileView, LatestResumeView)

urlpatterns = [
    path("profile/", LatestProfileView.as_view()),
    path("resume/", LatestResumeView.as_view())
]
