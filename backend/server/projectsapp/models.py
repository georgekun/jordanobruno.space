from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=20)
    short_description = models.TextField(max_length=100)
    full_descrtiption = models.CharField(max_length=1000, null=True)    
    main_image = models.FileField()
    
    def __str__(self):
        return f"{self.id} ==> {self.title} ==> {self.short_description}"


class ProjectImage(models.Model):
    name_image = models.CharField(max_length=10, null=True)
    image = models.FileField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name_image} ==> {self.project.title}"
