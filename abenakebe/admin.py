from django.contrib import admin
from abenakebe import models
# Register your models here.

class ImageJokeModelAdmin(admin.ModelAdmin):
    list_display = ('caption', )

class TextJokeModelAdmin(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(models.TextJoke, TextJokeModelAdmin)
admin.site.register(models.ImageJoke, ImageJokeModelAdmin)
admin.site.register(models.MemeJoke, ImageJokeModelAdmin)