from abenakebe import serializers, models 
from rest_framework import generics

# Create your views here.

class TextJokeView(generics.ListAPIView):
    serializer_class = serializers.TextJokeSerializer  
    queryset = models.TextJoke.objects.all() 

class ImageJokeView(generics.ListAPIView):
    serializer_class = serializers.ImageJokeSerializer 
    queryset = models.ImageJoke.objects.all() 

class MemeJokeView(generics.ListAPIView):
    serializer_class = serializers.MemeJokeSerializer 
    queryset = models.MemeJoke.objects.all() 