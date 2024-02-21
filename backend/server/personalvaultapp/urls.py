from django.urls import path

from .views import (LatestProfileView, LatestResumeView, ListSkillsView)

urlpatterns = [
    path("profile/", LatestProfileView.as_view()),
    path("resume/", LatestResumeView.as_view()), 
    path("skills/<str:type_skills>", ListSkillsView.as_view()), 
]
