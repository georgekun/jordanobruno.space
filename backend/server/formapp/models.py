from django.db import models

# Create your models here.


class Application(models.Model):
    sender_name = models.CharField(max_length=20)
    sender_contact = models.CharField(max_length=50)
    sender_comment = models.TextField(max_length=255)
    sender_ip = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (f"{self.created_at.date()}   =>   {self.sender_name}"
            f"   =>   {self.sender_contact}   =>   {self.sender_comment[:10]}")
