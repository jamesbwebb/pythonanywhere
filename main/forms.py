from django import forms

class CreateNewList(forms.Form):
# label is an optional argument but it'll show up before the input box so we have an idea what to type in here.
# max length is not optional
	name = forms.CharField(label="Name", max_length=200)
	check = forms.BooleanField(required=False)
