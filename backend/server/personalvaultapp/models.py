from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    avatar = models.FileField(upload_to="_my/profile/")
    number_phone = models.CharField(max_length=30)  
    email = models.CharField(max_length=30)
    telegram_link = models.CharField(max_length=20)
    vk_link = models.CharField(max_length=20)    
    update_at = models.DateTimeField(auto_now_add=True)



class Resume(models.Model):
    resume_html = models.FileField(upload_to="_my/resume/html/")
    resume_pdf = models.FileField(upload_to="_my/resume/pdf/")
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"{self.id} === {self.created_at}"

