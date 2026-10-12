from django.db import models

class Genre(models.Model):
    genre=models.CharField(max_length=100)

    def __str__(self):
        return self.genre

class Movie(models.Model):
    title=models.CharField(max_length=200)
    duration=models.IntegerField()
    age_range=models.IntegerField()
    image=models.ImageField(upload_to='movie_images/')
    genre=models.ForeignKey('Genre',on_delete=models.CASCADE,related_name='movies')

    def __str__(self):
        return self.title

class Feedback(models.Model):
    name=models.CharField(max_length=100)
    text=models.TextField()
