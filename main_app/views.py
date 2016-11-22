from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'homepage.html')

def viewpictures(request):

    return render(request, 'picturepage.html',{})
