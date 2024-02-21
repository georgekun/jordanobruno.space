from django.urls import path

from .views import (ListLatestProjectView, ListProjectView,
                    ProjectView, ProjectImagesView)

urlpatterns = [

    path('all/', ListProjectView.as_view()),
    path('latest/', ListLatestProjectView.as_view()),
    path('<int:id>/', ProjectView.as_view()),
    path('images/<int:id>/', ProjectImagesView.as_view()),

]
