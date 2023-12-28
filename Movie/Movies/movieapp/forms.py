from django import forms
from movieapp.models import addmodel

class addform(forms.ModelForm):
    class Meta:
        model=addmodel
        fields="__all__"
