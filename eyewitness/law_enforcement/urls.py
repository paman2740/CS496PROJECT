from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
     path('gallery/', views.gallery, name='gallery'),
     path('customer_register/',views.customer_register.as_view(), name='customer_register'),
     path('employee_register/',views.employee_register.as_view(), name='employee_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     path('home', views.gallery, name='gallery'),
     path('photo/<str:pk>/', views.viewPhoto, name='photo'),
     path('add/', views.addPhoto, name='add'),
     path('witnessList/', views.witnessList, name='witnessList'),
     path('addCase/', views.addCase, name='addCase'),
     path('addLineup/<str:pk>/', views.addLineup, name='addLineup'),
     
]