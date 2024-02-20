from rest_framework import serializers

from .models import Profile, Resume


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['id']



class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        exclude = ['id']

