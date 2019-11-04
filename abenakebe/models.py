from django.db import models

# Create your models here.

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

class TextLike(models.Model):
    joke = models.ForeignKey('TextJoke', on_delete=models.CASCADE, related_name='likes')

class ImageLike(models.Model):
    joke = models.ForeignKey('ImageJoke', on_delete=models.CASCADE, related_name='likes')

class MemeLike(models.Model):
    joke = models.ForeignKey('MemeJoke', on_delete=models.CASCADE, related_name='likes')





