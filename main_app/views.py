from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Picture
from .models import PictureForm

# Create your views here.
def home(request):
    form = PictureForm()
    return render(request,'homepage.html',{'form':form})


def viewpictures(request):
    p = Picture.objects.all()
    return render(request, 'picturepage.html', {'pictures':p})

def upload_images(request):
    form = PictureForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect('/')
