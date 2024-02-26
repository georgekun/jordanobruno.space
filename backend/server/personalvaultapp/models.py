from django.db import models
from django.core.validators import FileExtensionValidator

class Profile(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    
    avatar = models.FileField(
            upload_to="_my/profile/",
            validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg'])])
    
    number_phone = models.CharField(max_length=30)  
    email = models.CharField(max_length=30)
    telegram_link = models.CharField(max_length=20)
    vk_link = models.CharField(max_length=20)    
    update_at = models.DateTimeField(auto_now_add=True)



class Resume(models.Model):

    resume_html = models.FileField(
            upload_to="_my/resume/html/",
            validators=[FileExtensionValidator(allowed_extensions=['html'])])
    
    resume_pdf = models.FileField(
            upload_to="_my/resume/pdf/", 
            validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
                    
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"{self.id} === {self.created_at}"



class HardSkill(models.Model):
    title = models.CharField(max_length=20)
    percent = models.IntegerField()

    
    def __str__(self):
        return f"{self.title} == {self.percent}"


class SoftSkill(models.Model):
    title = models.CharField(max_length=20)
    percent = models.IntegerField()

    def __str__(self):
        return f"{self.title} == {self.percent}"
