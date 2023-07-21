from django.db import models


# Create your models here.

class KanaCheck(models.Model):
	text = models.CharField(max_length=10)
	img = models.IntegerField()

	def __str__(self):
		return self.text
