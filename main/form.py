from django import forms

class AnalysisForm(forms.Form):
    userName = forms.CharField(max_length=255)
    tweets = forms.CharField(max_length=255)