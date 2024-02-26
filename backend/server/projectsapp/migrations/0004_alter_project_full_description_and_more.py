# Generated by Django 5.0.2 on 2024-02-26 12:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectsapp', '0003_alter_project_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='full_description',
            field=models.FileField(upload_to='_projects/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['html'])]),
        ),
        migrations.AlterField(
            model_name='project',
            name='main_image',
            field=models.FileField(upload_to='_project/images/main/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.FileField(upload_to='_project/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg'])]),
        ),
    ]
