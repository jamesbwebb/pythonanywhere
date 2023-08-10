from django import forms

class KanaChecker(forms.Form):
#	answer=forms.CharField(label='answer', max_length=10)
	guess=forms.CharField(label="guess", max_length=10)
