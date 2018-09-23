from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .forms import MovieForm, SignUpForm
from .models import Movie

def home(request):
    status = ''
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('home')
    else:
        form = MovieForm()
    # put render outside 'else' block, so user can see the error messages
    return render(request, 'movie/index.html', {'form': form, 'movies': Movie.objects.all(), 'status': status })

def edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    status = 'success'
    titleValue = Movie.objects.filter(pk=pk).values('title')[0];
    movie_title = titleValue['title']
    
    if request.method == 'POST':
        post_form = MovieForm(request.POST, instance=movie)
        if post_form.is_valid():
            post_form.save()
            return render(request, 'movie/edit.html', {'form': post_form, 'status': status, 'movie_title': movie_title })
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie/edit.html', {'form': form, 'movie_title': movie_title })

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return HttpResponseRedirect('home')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birthdate = form.cleaned_data.get('birthdate')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.address = form.cleaned_data.get('address')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return render(request, 'movie/login.html', { })
    else:
        form = SignUpForm()
    return render(request, 'movie/signup.html', { 'form': form })




