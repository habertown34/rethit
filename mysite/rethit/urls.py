from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upvote', views.upvote, name='upvote'),
    path('downvote', views.downvote, name='downvote')
]