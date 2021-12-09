from django.urls import path
from .views import login_page, register,logout_user

urlpatterns= [
path('', login_page, name='login'),
path('register', register, name='register'),
path('logout',logout_user, name='logout')
]