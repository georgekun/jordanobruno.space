# Generated by Django 5.0.2 on 2024-02-27 11:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
                ('avatar', models.FileField(upload_to='_my/profile/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])),
                ('number_phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('telegram_link', models.CharField(max_length=100)),
                ('vk_link', models.CharField(max_length=100)),
                ('github_link', models.CharField(max_length=100)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_html', models.FileField(upload_to='_my/resume/html/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['html'])])),
                ('resume_pdf', models.FileField(upload_to='_my/resume/pdf/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
