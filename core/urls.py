from django.urls import path
from core import views

urlpatterns = [
    path('hello/', views.index),
    path('timedate/', views.timedate)

]
