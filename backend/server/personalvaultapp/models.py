from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    avatar = models.FileField(upload_to="_my")
    number_phone = models.CharField(max_length=30)  
    email = models.CharField(max_length=30)
    telegram_link = models.CharField(max_length=20)
    vk_link = models.CharField(max_length=20)    
    update_at = models.DateTimeField(auto_now_add=True)



class Resume(models.Model):
    specialization = models.TextField(max_length=255)
    education = models.TextField(max_length=255)
    experience = models.TextField(max_length=255)
    courses = models.TextField(max_length=255)

    resume_pdf = models.FileField(upload_to="_my")
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"{self.title} === {self.value[:10]}"

