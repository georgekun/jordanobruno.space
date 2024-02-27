from rest_framework import serializers
from django.core.files.storage import default_storage

from .models import Profile, Resume 


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['id']



class ResumeSerializer(serializers.ModelSerializer):
    resume_html = serializers.SerializerMethodField()
    resume_pdf = serializers.SerializerMethodField()

    class Meta:
        model = Resume
        exclude = ['id']
        
    def get_resume_html(self, instance):
        if not instance or not instance.resume_html:
            return None

        with open(instance.resume_html.path, "rb") as file:
            return file.read()

    def get_resume_pdf(self, instance):
        if instance.resume_pdf:
            return default_storage.url(instance.resume_pdf.name)
        return None


