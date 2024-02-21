from rest_framework import views, generics, status, response

from .models import Project, ProjectImage

from .serializers import (ProjectSerializer,
                          ProjectListSerializer,
                          ProjectImagesSerializer)



class ListProjectView(generics.ListAPIView):
    """ Ендпоинт для получения всех проектов """

    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer


class ListLatestProjectView(generics.ListAPIView):
    """ Ендпоинт для получения последних трёх проектов """

    queryset = Project.objects.all().order_by('-id')[:3]
    serializer_class = ProjectListSerializer


class ProjectView(generics.RetrieveAPIView):
    """ Ендпоинт для получения информации по проекту """
    
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'


class ProjectImagesView(generics.ListAPIView):
    """ Ендпоинт для получения списка\
            фотографий конткретного проекта """
    
    serializer_class = ProjectImagesSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get("id")
        project = Project.objects.filter(id=pk).first()
        return ProjectImage.objects.filter(project=project).all()

    
