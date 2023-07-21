from django import forms

class KanaChecker(forms.Form):
	entry=forms.CharField(label='entry', max_length=10)
	img=forms.IntegerField()
