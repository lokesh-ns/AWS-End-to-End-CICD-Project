from django.urls import path
from .views import greet_func

urlpatterns = [
    path('', view=greet_func),
]
