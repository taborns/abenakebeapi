from django.contrib import admin
from abenakebe import models
# Register your models here.

class ImageJokeModelAdmin(admin.ModelAdmin):
    list_display = ('caption', )

class TextJokeModelAdmin(admin.ModelAdmin):
    list_display = ('title', )

class JokeModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'content' )

admin.site.register(models.Joke, JokeModelAdmin)
admin.site.register(models.TextJoke, TextJokeModelAdmin)
admin.site.register(models.ImageJoke, ImageJokeModelAdmin)
admin.site.register(models.MemeJoke, ImageJokeModelAdmin)