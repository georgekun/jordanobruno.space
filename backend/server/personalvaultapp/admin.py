from django.contrib import admin

from .models import Resume, Profile


admin.site.register([Resume, Profile])
