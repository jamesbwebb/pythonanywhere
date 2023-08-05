from django.db import models


# Create your models here.

class KanaCheck(models.Model):
#	text = models.TextField()
	text = models.CharField(max_length=10)
	hir = models.CharField(max_length=10, default='null')

	def __str__(self):
		output = self.text + ' ' + self.hir
		return output
