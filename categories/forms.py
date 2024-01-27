from django import forms
from .import models



class Add_Category(forms.ModelForm):
    class Meta:
        model=models.Category
        fields='__all__'