from django.db import models
from django import forms

# Create your models here.
class Picture(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }
        fields = ['name','description','img_url']
