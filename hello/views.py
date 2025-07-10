import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from hello.forms import MovieForm
from hello.models import Movie
from django.views.generic import ListView
from django.db.models import Q


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = Movie

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "hello/about.html")


def movie_list(request):
    query = request.GET.get("q", "")
    movies = Movie.objects.all().order_by("release_date")
    if query:
        movies = movies.filter(Q(name__icontains=query))
    return render(request, "hello/movie_list.html", {"movies": movies, "query": query})

def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movie_list")
    else:
        form = MovieForm()
    return render(request, "hello/add_movie.html", {"form": form})

def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect("movie_list")

def favorite_list(request):
    movies = Movie.objects.filter(is_favorite=True).order_by("release_date")
    return render(request, "hello/favorite_list.html", {"movies": movies})
