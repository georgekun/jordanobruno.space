from rest_framework import generics

from .models import Profile, Resume
from .serializers import ProfileSerializer, ResumeSerializer

class LatestProfileView(generics.RetrieveAPIView):
    """ Ендпоинт для получения последней версии профиля """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.queryset.last()



class LatestResumeView(generics.RetrieveAPIView):
    """ Ендпоинт  для получения последней версии резюме """
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    def get_object(self):
        return self.queryset.last()


