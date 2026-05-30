from django.shortcuts import render, get_object_or_404
from .models import Movie, Show


def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    shows = Show.objects.filter(movie=movie)

    return render(request, 'movie_detail.html', {
        'movie': movie,
        'shows': shows
    })