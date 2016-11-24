from django.shortcuts import render
from .models import Picture

# Create your views here.
def home(request):
    return render(request,'homepage.html')

def viewpictures(request):
    p = Picture.objects.all()
    return render(request, 'picturepage.html', {'pictures':p})
