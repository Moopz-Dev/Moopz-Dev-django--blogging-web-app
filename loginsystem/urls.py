from atexit import register
from django.urls import path
from .views import index
urlpatterns = [
    path('register', index, name="register")
]
