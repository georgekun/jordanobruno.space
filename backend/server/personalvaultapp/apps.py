import os
import sys
from django.apps import AppConfig
from django.conf import settings



class PersonalvaultappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personalvaultapp'


    def ready(self):
        from django.contrib.auth.models import User
        from django.db.utils import IntegrityError

        if 'migrate' not in sys.argv:
            # Создание суперпользователя
            try:
                user = User.objects.filter(username="admin").first()
                if user:
                    return
                User.objects.create_superuser(
                    "admin",
                    'admin@example.com',
                    "admin")
                print('Superuser created successfully!')
            except IntegrityError:
                print('Superuser already exists.')
