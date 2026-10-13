from django.urls import path
from .views import homeView,movie_info,movie_create,movie_delete,create_feedback,movie_update,feedback_view,update_feedback,delete_feedback
urlpatterns=[
    path('',homeView,name='home'),
    path('<int:pk>/',movie_info,name='movie_info'),
    path('create/',movie_create,name='movie_create'),
    path('contact/',create_feedback,name='contact'),
    path('<int:pk>/update/',movie_update,name='movie_update'),
    path('<int:pk>/delete/',movie_delete,name='movie_delete'),
    path('feedback/', feedback_view, name='feedback'),
    path('feedback/<int:pk>/update/', update_feedback, name='update_feedback'),
    path('feedback/<int:pk>/delete/', delete_feedback, name='delete_feedback'),
]