from abenakebe import serializers, models 
from rest_framework import generics
from rest_framework.views import APIView
from collections import namedtuple 
from rest_framework.response import Response

# Create your views here.
Feed = namedtuple('Feed', ('text_jokes', 'image_jokes','meme_jokes'))

class JokeView(generics.ListAPIView):
    serializer_class = serializers.JokeSerializer  
    queryset = models.Joke.objects.all() 


class TextJokeView(generics.ListAPIView):
    serializer_class = serializers.JokeSerializer  
    queryset = models.Joke.objects.filter(joke_type='text') 

class ImageJokeView(generics.ListAPIView):
    serializer_class = serializers.JokeSerializer  
    queryset = models.Joke.objects.filter(joke_type='image') 

class MemeJokeView(generics.ListAPIView):
    serializer_class = serializers.JokeSerializer  
    queryset = models.Joke.objects.filter(joke_type='meme') 

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


class JokeLikeView(generics.CreateAPIView):

    serializer_class = serializers.JokeLikeSerializer 
    queryset = models.JokeLike.objects.all()

    def perform_create(self, serializer):
        like = serializer.save()
        joke = like.joke
        joke.like_count += 1
        joke.save()

class TextLikeView(generics.CreateAPIView):

    serializer_class = serializers.TextLikeSerializer 
    queryset = models.TextLike.objects.all()

    def perform_create(self, serializer):
        like = serializer.save()
        joke = like.joke
        joke.like_count += 1
        joke.save()

class ImageLikeView(generics.CreateAPIView):

    serializer_class = serializers.ImageLikeSerializer 
    queryset = models.TextLike.objects.all()
    
    def perform_create(self, serializer):
        like = serializer.save()
        joke = like.joke
        joke.like_count += 1
        joke.save()

    
class MemeLikeView(generics.CreateAPIView):

    serializer_class = serializers.MemeLikeSerializer 
    queryset = models.TextLike.objects.all()
    
    def perform_create(self, serializer):
        like = serializer.save()
        joke = like.joke
        joke.like_count += 1
        joke.save()
