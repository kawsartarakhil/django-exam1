from django.urls import path
from .views import homeView,movie_info,movie_create,movie_delete,create_feedback
urlpatterns=[
    path('',homeView,name='home'),
    path('<int:pk>/',movie_info,name='movie_info'),
    path('create/',movie_create,name='movie_create'),
    path('contact/',movie_info,name='contact'),
    path('<int:pk>/update/',movie_info,name='movie_update'),
    path('<int:pk>/delete/',movie_delete,name='movie_delete'),
    path('contact',create_feedback,name='contact')

]