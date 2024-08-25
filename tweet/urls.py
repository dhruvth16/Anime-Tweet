from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('register/', views.user_register, name='user_register'),
    path('create/', views.create_tweet, name='create_tweet'),
    path('edit/<int:tweet_id>/', views.edit_tweet, name='edit_tweet'),
    path('delete/<int:tweet_id>/', views.delete_tweet, name='delete_tweet'),
    path('search/', views.tweet_search, name='tweet_search'),
] 