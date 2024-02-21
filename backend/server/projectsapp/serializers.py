from rest_framework import serializers

from .models import Project, ProjectImage


class ProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'main_image']


class ProjectSerializer(serializers.ModelSerializer):
    full_description = serializers.SerializerMethodField()    
    
    class Meta:
        model = Project
        fields = '__all__'
    
    def get_full_description(self, obj):
        if not obj or not obj.full_description:
            return None

        try:
            with open(obj.full_description.path, "r", encoding='utf-8') as file:
                return file.read()
        except (FileNotFoundError, IOError):
            return None

class ProjectImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectImage
        fields = ['image']
