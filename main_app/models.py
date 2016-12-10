from django.db import models
from django import forms
from django.contrib.auth.models import User


# Create your models here.
class Picture(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name
class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }
        fields = ['name','description','img_url']

class SignupForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput())
    email=forms.CharField(max_length=100)
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)

class LogInForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())