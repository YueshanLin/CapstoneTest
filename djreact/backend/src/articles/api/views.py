"""
Views module
"""

from rest_framework.generics import ListAPIView, RetrieveAPIView

from articles.models import Article, movie, artist, role
from .serializers import ArticleSerializer, MovieSerializer, ArtistSerializer, RoleSerializer

class ArticleListView(ListAPIView):
    """
    Article list view class.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveAPIView):
    """
    Article list view class.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class modelListView(ListAPIView):
    queryset = movie.objects.all()
    serializer_class = MovieSerializer


class modelDetailView(RetrieveAPIView):
    queryset = movie.objects.all()
    serializer_class = MovieSerializer


class artistListView(ListAPIView):
    queryset = artist.objects.all()
    serializer_class = ArtistSerializer


class artistDetailView(RetrieveAPIView):
    queryset = movie.objects.all()
    serializer_class = ArtistSerializer


class roleListView(ListAPIView):
    queryset = role.objects.all()
    serializer_class = RoleSerializer


class roleDetailView(RetrieveAPIView):
    queryset = movie.objects.all()
    serializer_class = RoleSerializer
