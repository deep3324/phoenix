from django.contrib import admin
from django.urls import path
from PhoenixApp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('clubs', views.clubs, name="clubs"),
    path('events', views.events, name="events"),
    path('blogs', views.blogs, name="blogs"),
    path('gallery', views.gallery, name="gallery"),
    path('webteam', views.webteam, name="webteam"),
    path('contact', views.contact, name="contact"),
    path('avenir', views.avenir, name="avenir"),
    path('brainstormer', views.brainstormer, name="brainstormer"),
    path('aavahan', views.aavahan, name="aavahan"),
    path('cybernix', views.cybernix, name="cybernix"),
    path('eloquense', views.eloquense, name="eloquense"),
    path('robonix', views.robonix, name="robonix"),
    path('lensified', views.lensified, name="lensified"),
    path('nirmaan', views.nirmaan, name="nirmaan"),
    path('review', views.review, name="review"),
    path('<str:slug>/result', views.result, name="result"),
    # path('membership', views.membership, name="membership"),
    path('blogs/<int:myid>', views.blog, name="blog"),
    # path('events/Creativarty', views.Creativarty, name="Creativarty"),
    # path('events/Creativarty/confirmation/', views.Confirmation, name="Confirmation"),
    path('events/Quizomania', views.Quizomania, name="Quizomania"),
    path('events/Quizomania/confirmation/', views.confirmation, name="confirmation"),

]
