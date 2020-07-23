from django.urls import path
from . import views
from django.urls import path, include
from .views import (
    HomeView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
