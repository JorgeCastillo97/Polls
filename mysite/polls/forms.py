from django import forms
from .models import *

class NewPollForm(forms.Form):
    question_input = forms.CharField(label='Enter your Question:', max_length=100, min_length=1, required=True)
    choice_1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'choice'}), label='Choice 1:', min_length=1, max_length=30, required=True)
    choice_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'choice'}), label='Choice 2:', min_length=1, max_length=30, required=True)

    # We can display the form 'as_table' or 'as_p'
    #