from django.contrib import admin
from .models import Movie, Show


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'release_date')
    search_fields = ('title', 'language')
    list_filter = ('language', 'release_date')


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('movie', 'timing')
    search_fields = ('movie__title',)