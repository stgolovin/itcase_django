from django.contrib import admin
from .models import Good, Image, Parameter
# Register your models here.

admin.site.register(Good)
admin.site.register(Image)
admin.site.register(Parameter)