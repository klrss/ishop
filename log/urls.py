from django.urls import path
from .views import login_page, register

urlpatterns= [
path('login', login_page, name='login'),
path('register', register, name='register'),
]