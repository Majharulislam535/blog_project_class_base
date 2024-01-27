from django import forms
from .import models



class Add_Post(forms.ModelForm):
    class Meta:
        model=models.Post
        exclude=['author']

class CommentForm(forms.ModelForm):
    class Meta:
        model=models.Comment
        fields=['name','email','body']

