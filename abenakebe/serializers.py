from rest_framework import serializers 
from abenakebe import models 

class TextJokeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TextJoke 
        fields = '__all__'

class ImageJokeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ImageJoke 
        fields = '__all__'



class MemeJokeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MemeJoke
        fields = '__all__'

class FeedSerializer(serializers.Serializer):

    text_jokes = TextJokeSerializer(many=True)
    image_jokes = ImageJokeSerializer(many=True)
    meme_jokes = MemeJokeSerializer(many=True)

class TextLikeSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()

    def get_like_count(self, obj):
        return obj.joke.like_count

    class Meta:
        model = models.TextLike
        fields = '__all__'

class ImageLikeSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()

    def get_like_count(self, obj):
        return obj.joke.like_count

    class Meta:
        model = models.ImageLike
        fields = '__all__'

class MemeLikeSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()

    def get_like_count(self, obj):
        return obj.joke.like_count

    class Meta:
        model = models.MemeLike
        fields = '__all__'

