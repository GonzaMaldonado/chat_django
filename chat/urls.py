from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<str:room>', views.Room.as_view(), name='room'),
    path('checkview', views.checkview, name='checkview'),
]