from django.urls import path

from .views import (LatestProfileView, LatestResumeView, DownloadResumeView)

urlpatterns = [
    path("profile/", LatestProfileView.as_view()),
    path("resume/", LatestResumeView.as_view()),
    path("resume-pdf/", DownloadResumeView.as_view()),
]
