from django import forms
from .models import imgModel

class imgModelForm(forms.ModelForm):
    class Meta:
        model=imgModel
        fields='__all__'
        labels={'img':''}