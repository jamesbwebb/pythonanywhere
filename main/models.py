from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# database object
class ToDoList(models.Model):
# Define attributes/entries name, followed by field type.
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Item(models.Model):
	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()

	def __str__(self):
		return self.text
