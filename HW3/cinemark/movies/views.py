from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm
from rest_framework import generics
from .serializers import MovieSerializer

# Create your views here.

class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie-list.html', {'movies': movies})

def movie_details(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movies/movie-details.html', {'movie': movie})

def movie_add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie-add.html', {'form': form})

def movie_update(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_details', id=movie.id)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie-update.html', {'form': form, 'movie': movie})

def movie_delete(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies/movie-list.html', {'movie': movie})

def redirect_view(request):
    return redirect('/movie/list/')