# Generated by Django 5.0.2 on 2024-02-20 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalvaultapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
