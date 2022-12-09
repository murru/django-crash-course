from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Movie

def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')

    return render(request, 'movies/add.html')

def home(request):
    return HttpResponse("Home page")