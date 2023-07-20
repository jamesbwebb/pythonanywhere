from django.urls import path
from . import views

app_name = 'learnkana'

urlpatterns = [

path('learn/', views.learn, name='learnkana'),

]
