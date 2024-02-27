from rest_framework import serializers
from django.core.files.storage import default_storage

from .models import Profile, Resume 


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['id']



class FileUrlField(serializers.FileField):
    def to_internal_value(self, data):
        try:
            URLValidator()(data)
        except ValidationError as e:
            raise ValidationError('Invalid Url')

        # download the contents from the URL
        file, http_message = urlretrieve(data)
        file = File(open(file, 'rb'))
        return super(FileUrlField, self).to_internal_value(ContentFile(file.read(), name=file.name))


class ResumeSerializer(serializers.ModelSerializer):
    resume_html = serializers.SerializerMethodField()
    resume_pdf = FileUrlField()

    class Meta:
        model = Resume
        exclude = ['id']
        
    def get_resume_html(self, instance):
        if not instance or not instance.resume_html:
            return None

        with open(instance.resume_html.path, "rb") as file:
            return file.read()



