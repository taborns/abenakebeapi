from abenakebe import serializers, models 
from rest_framework import generics
from rest_framework.views import APIView
from collections import namedtuple 
from rest_framework.response import Response

# Create your views here.
Feed = namedtuple('Feed', ('text_jokes', 'image_jokes','meme_jokes'))

class TextJokeView(generics.ListAPIView):
    serializer_class = serializers.TextJokeSerializer  
    queryset = models.TextJoke.objects.all() 

class ImageJokeView(generics.ListAPIView):
    serializer_class = serializers.ImageJokeSerializer 
    queryset = models.ImageJoke.objects.all() 

class MemeJokeView(generics.ListAPIView):
    serializer_class = serializers.MemeJokeSerializer 
    queryset = models.MemeJoke.objects.all() 

class FeedView(APIView):
    def get(self, request, format=None):
        serializer = serializers.FeedSerializer(
            Feed(
                text_jokes = models.TextJoke.objects.all(),
                image_jokes = models.ImageJoke.objects.all(),
                meme_jokes = models.MemeJoke.objects.all()
            )
        )

        return Response( serializer.data )
