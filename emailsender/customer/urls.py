from django.contrib import admin
from django.urls import path,include
from customer import views

urlpatterns = [
    path('email/', views.email, name='email'), 
    path('email_info/', views.email_info, name='email_info'),    
]
