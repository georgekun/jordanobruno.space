from django.contrib import admin

from .models import Resume, Profile, HardSkill, SoftSkill


admin.site.register([Resume, Profile, HardSkill, SoftSkill])
