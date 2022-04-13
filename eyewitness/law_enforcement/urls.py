from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
     path('gallery/', views.gallery, name='gallery'),
     path('witness_register/',views.witness_register.as_view(), name='witness_register'),
     path('officer_register/',views.officer_register.as_view(), name='officer_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     path('home', views.gallery, name='gallery'),
     path('photo/<str:pk>/', views.viewPhoto, name='photo'),
     path('add/', views.addPhoto, name='add'),
     path('witnessList/', views.witnessList, name='witnessList'),
     path('addCase/', views.addCase, name='addCase'),
     path('addLineup/<str:pk>/', views.addLineup, name='addLineup'),
     path('lineUp/', views.lineUp, name='lineUp'),
     path('search_photo/', views.search_photo, name='search_photo'),
     path('witness_view/', views.witness_view, name='witness_view'),
     path('photoWitness/<str:pk>/', views.photoWitness, name='photoWitness'),
     path('finalSubmit/<str:pk>/', views.finalSubmit, name='finalSubmit'),
     path('submittedPhoto/', views.submittedPhoto, name='submittedPhoto'),
]