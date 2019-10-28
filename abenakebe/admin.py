from django.contrib import admin
from abenakebe import models
# Register your models here.

admin.site.register(models.TextJoke)
admin.site.register(models.ImageJoke)
admin.site.register(models.MemeJoke)