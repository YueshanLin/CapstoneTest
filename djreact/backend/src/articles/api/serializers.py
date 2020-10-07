"""
Serializers module.
"""

from rest_framework import serializers
from articles.models import Article, movie, artist, role

class ArticleSerializer(serializers.ModelSerializer):
    """
    Article serializer class.
    """
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = ('id', 'title', 'artist')
        depth = 1

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = artist
        fields = ('id', 'name')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = role
        fields = ('id', 'role_name', 'artist', 'movie')
