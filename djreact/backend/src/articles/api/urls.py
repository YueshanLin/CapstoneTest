"""
Url module.
"""

from django.urls import path

from .views import ArticleListView, ArticleDetailView
from .views import modelListView, modelDetailView
from .views import artistListView, artistDetailView
from .views import roleListView, roleDetailView

urlpatterns = [
    #path('', ArticleListView.as_view()),
    path('', modelListView.as_view()),
    #path('<pk>', ArticleDetailView.as_view()),
    path('movie', modelListView.as_view()),
    path('movie/<pk>', modelDetailView.as_view()),
    path('artist', artistListView.as_view()),
    path('artist/<pk>', artistDetailView.as_view()),
    path('role', roleListView.as_view()),
    path('role/<pk>', roleDetailView.as_view()),
]
