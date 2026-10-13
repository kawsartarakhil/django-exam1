from django.shortcuts import render, redirect, get_object_or_404
from .models import Genre, Movie, Feedback


def homeView(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', context={'movies': movies})


def movie_info(request, pk):
    movie = get_object_or_404(Movie, id=pk)
    return render(request, 'info.html', context={'movie': movie})


def movie_create(request):
    genre = Genre.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        duration = request.POST.get('duration')
        age_range = request.POST.get('age_range')
        image = request.FILES.get('image')
        genre_id = request.POST.get('genre')
        genre_obj = get_object_or_404(Genre, id=genre_id)
        Movie.objects.create(title=title, duration=duration, age_range=age_range, image=image, genre=genre_obj)
        return redirect('home')
    return render(request, 'create_movie.html', context={'genre': genre})


def movie_update(request, pk):
    movie = get_object_or_404(Movie, id=pk)
    genre = Genre.objects.all()
    if request.method == 'POST':
        movie.title = request.POST.get('title')
        movie.duration = request.POST.get('duration')
        movie.age_range = request.POST.get('age_range')
        if request.FILES.get('image'):
            movie.image = request.FILES.get('image')
        genre_id = request.POST.get('genre')
        genre_obj = get_object_or_404(Genre, id=genre_id)
        movie.genre = genre_obj
        movie.save()
        return redirect('home')
    return render(request, 'update_movie.html', context={'movie': movie,'genre': genre})


def movie_delete(request, pk):
    movie = get_object_or_404(Movie, id=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('home')
    return render(request, 'movie_delete.html', context={'movie': movie})


def create_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')
        Feedback.objects.create(name=name, text=text)
        return redirect('home')
    return render(request, 'contact.html')



def feedback_view(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback.html', context={'feedbacks': feedbacks})



def update_feedback(request, pk):
    feedback = get_object_or_404(Feedback, id=pk)
    if request.method == 'POST':
        feedback.name = request.POST.get('name')
        feedback.text = request.POST.get('text')
        feedback.save()
        return redirect('feedback')
    return render(request, 'update_feedback.html', context={'feedback': feedback})


def delete_feedback(request, pk):
    feedback = get_object_or_404(Feedback, id=pk)
    if request.method == 'POST':
        feedback.delete()
        return redirect('feedback')
    return render(request, 'delete_feedback.html', context={'feedback': feedback})


