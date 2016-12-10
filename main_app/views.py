from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import Picture
from .models import PictureForm
from .models import SignupForm
from .models import LogInForm

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
        picture = form.save(commit=False)
        picture.user = request.user
        picture.save()
        return HttpResponseRedirect('/')

def sign_up(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            e = form.cleaned_data['email']
            f = form.cleaned_data['first_name']
            l = form.cleaned_data['last_name']
            user = User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            user.save()
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form':form})

def log_in(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u,password=p)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/')
                else:
                    print('This account has been disabled!')
            else:
                print('The username and password were incorrect')
    else:
        form = LogInForm()
        return render(request, 'login.html', {'form':form})

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/pictures')