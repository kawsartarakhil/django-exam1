from django.shortcuts import render,redirect,get_object_or_404
from .models import Genre,Movie,Feedback

def homeView(request):
    movies=Movie.objects.all()
    return render(request,'home.html',context={'movies':movies})

def movie_info(request,pk):
    movie=Movie.objects.get(id=pk)
    return render(request,'info.html',context={'movie':movie})

def movie_create(request):
    if request.method=='POST':
        title=request.POST.get('title')
        duration=request.POST.get('duration')
        age_range=request.POST.get('age_range')
        image=request.FILES.get('image')
        genre_id=Genre.POST.get()
        genre_obj=get_object_or_404(Genre,pk=genre_id)
        Movie.objects.create(title=title,duration=duration,age_range=age_range,image=image,genre=genre_obj)
        return redirect('home')
    return render(request,'create_movie.html',context={'genre':genre_obj})

def movie_update(request,pk):
    movie=Movie.objects.get(id=pk)
    genre=Genre.objects.all()
    if request.method=='POST':
        movie.title=request.POST.get('title')
        movie.duration=request.POST.get('duration')
        movie.age_range=request.POST.get('age_range')
        if request.Files.get('image'):
            movie.image=request.FILES.get('image')
        genre.genre=Genre.POST.get()
        genre.genre_obj=get_object_or_404()
        movie.save()
        return redirect('home')
    return render(request,'update_movie.html',context={'genre':genre,'movie':movie})


def movie_delete(request,pk):
    movie=Movie.objects.get(id=pk)
    if request.method=='POST':
        movie.delete()
        return redirect('home')
    return render(request,'movie_delete.html',context={'movie':movie})

def create_feedback(request):
    if request.method=='POST':
        name=request.POST.get('name')
        text=request.POST.get('text')
        Feedback.objects.create(name=name,text=text)
        return redirect('home')
    return render(request,'contact.html')


