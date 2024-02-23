from django.contrib import admin
from .models import Report, File, Profile

# Register your models here.
admin.site.register(Report)
admin.site.register(File)
admin.site.register(Profile)