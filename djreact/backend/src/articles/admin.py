from django.contrib import admin

from .models import Article, movie, artist, role, movieAdmin, artistAdmin

admin.site.register(Article)

admin.site.register(movie, movieAdmin)
admin.site.register(artist, artistAdmin)
admin.site.register(role)
