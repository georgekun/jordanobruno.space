from rest_framework import generics

from .models import Profile, Resume, HardSkill, SoftSkill
from .serializers import (ProfileSerializer, SkillSerializer, ResumeSerializer)

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


class ListSkillsView(generics.ListAPIView):
    """ Ендпоинт для получения списка\
            скилов, принмает строку 'soft'/'hard'""" 
    serializer_class = SkillSerializer
    
    def get_queryset(self):
        type_skills = self.kwargs.get("type_skills")
        if type_skills not in ['soft', 'hard']:
            return None

        if type_skills == 'soft':
            model = SoftSkill
        else:
            model = HardSkill
        
        return model.objects.all()

