from django import forms

class CreateNewAd(forms.Form):
# These are examples, I'll have to check with coursera to figure out how I need to build
# this form.
        name = forms.CharField(label="Name", max_length=200)
        check = forms.BooleanField(required=False)
