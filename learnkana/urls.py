from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'learnkana'

urlpatterns = [

path ('', views.Learn.as_view(), name='all'),
path('learnHiragana/', views.learnHiragana, name='learnkana'),

]
