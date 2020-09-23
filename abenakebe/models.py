from django.db import models

# Create your models here.

class Joke( models.Model ):
    title = models.CharField(max_length=150)
    content = models.TextField(null=True, blank=True) 
    image = models.FileField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)

    joke_type = models.CharField( max_length = 10, choices = (
        ('text', 'Text'),
        ('meme', 'Meme'),
        ('image', 'Image')
    ))
    
    class Meta:
        ordering = '-created_at',

class TextJoke(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
    
    class Meta:
        ordering = '-created_at',

class ImageJoke(models.Model):
    caption = models.CharField(max_length=150)
    image = models.FileField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
    
    class Meta:
        ordering = '-created_at',

class MemeJoke(models.Model):
    caption = models.CharField(max_length=150)
    image = models.FileField(upload_to='images/')  
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
    
    class Meta:
        ordering = '-created_at',

class JokeLike(models.Model):
    joke = models.ForeignKey('Joke', on_delete=models.CASCADE, related_name='likes')

class TextLike(models.Model):
    joke = models.ForeignKey('TextJoke', on_delete=models.CASCADE, related_name='likes')

class ImageLike(models.Model):
    joke = models.ForeignKey('ImageJoke', on_delete=models.CASCADE, related_name='likes')

class MemeLike(models.Model):
    joke = models.ForeignKey('MemeJoke', on_delete=models.CASCADE, related_name='likes')





