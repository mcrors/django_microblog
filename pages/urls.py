from django.urls import path
from .views import helloWorldView

urlpatterns = [
    path('', helloWorldView, name='hello')
]
