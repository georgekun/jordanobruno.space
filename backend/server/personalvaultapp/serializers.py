from rest_framework import serializers

from .models import Profile, Resume


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['id']



class ResumeSerializer(serializers.ModelSerializer):
    resume_html = serializers.SerializerMethodField()
    
    class Meta:
        model = Resume
        exclude = ['id']
        
    def get_resume_html(self, instance):
        if not instance or not instance.resume_html:
            return None

        with open(instance.resume_html.path, "rb") as file:
            return file.read()
