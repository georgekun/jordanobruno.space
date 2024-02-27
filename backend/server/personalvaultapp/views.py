from django.http import FileResponse
from rest_framework import generics, views

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


class DownloadResumeView(views.APIView):

    def get(self, request):
        resume = Resume.objects.all().last()
        if resume and resuem.resume_pdf:
            file = resuem.resume_pdf
            filename = format_filename(file.name)
            return FileResponse(open(file.path, 'rb'), filename=filename,   status = status.HTTP_200_OK)
        else:
            return Response({}, status = status.HTTP_404_NOT_FOUND)
   

