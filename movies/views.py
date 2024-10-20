from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    movies = ['Tommy Boy', 'The Big Lebowski', 'The Matrix', 'The Dark Knight', 'Inception']
    return render(request, 'movies/index.html', {'movies': movies})

def about(request):
  return render(request, 'movies/about.html', {})

