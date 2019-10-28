from django.db import models

# Create your models here.

class TextJoke(models.Model):
    content = models.TextField() 

class ImageJoke(models.Model):
    caption = models.CharField(max_length=150)
    image = models.FileField(upload_to='images/')

class MemeJoke(models.Model):
    caption = models.CharField(max_length=150)
    image = models.FileField(upload_to='images/')  

