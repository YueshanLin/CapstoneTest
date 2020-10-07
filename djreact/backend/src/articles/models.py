"""
Model module.
"""

from django.db import models
from django.contrib import admin


class Article(models.Model):
    """
    Article class.
    """
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title


class artist(models.Model):
    name = models.CharField(max_length=200)


class movie(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ManyToManyField(artist, related_name='actor', through='role')


class role(models.Model):
    role_name = models.CharField(max_length=100)
    artist = models.ForeignKey(artist, on_delete=models.CASCADE)
    movie = models.ForeignKey(movie, on_delete=models.CASCADE)


class role_inline(admin.TabularInline):
    model = role
    extra = 1


class artistAdmin(admin.ModelAdmin):
    inline = (role_inline,)


class movieAdmin(admin.ModelAdmin):
    inline = (role_inline,)

