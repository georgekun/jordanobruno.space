from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    type_project = models.CharField(max_length=50)
    stack = models.CharField(max_length=255)
    full_description = models.FileField(upload_to="_projects/")    
    main_image = models.FileField(upload_to="_project/images/main/")
    
    def __str__(self):
        return f"{self.id} ==> {self.title}"


class ProjectImage(models.Model):
    name_image = models.CharField(max_length=10, null=True)
    image = models.FileField(upload_to="_project/images/")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name_image} ==> {self.project.title}"
