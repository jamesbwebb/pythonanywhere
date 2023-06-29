from django.urls import path
from . import views

# I don't know what purpose the "app_name" variable serves...
app_name = 'main'

urlpatterns = [
# for no additional url path the view (from the views.py file) = the name variable
# passed into the path function.

# This will pass an id variable, encapsulating the in, to the index funcion
path("<int:id>", views.index, name="index"),
path("",views.home, name="home"),
path("create/", views.create, name="create"),

]
