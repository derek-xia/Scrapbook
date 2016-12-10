"""Webpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from main_app import views

urlpatterns = [
    url(r'upload_picture/$', views.home, name='home'),
    url(r'^$', views.viewpictures, name='viewpictures'),
    url(r'^upload_picture/upload_image/$', views.upload_images, name='uploadimages'),

    url(r'^signup/$',views.sign_up, name='signup'),
    url(r'^login/$',views.log_in, name='login'),
    url(r'^logout/$',views.log_out, name='logout'),
    url(r'^(\w+)/$',views.user_page, name='userpage')
]

if settings.DEBUG:
 urlpatterns += [
 url(r'^media/(?P<path>.*)$', serve,
 {'document_root': settings.MEDIA_ROOT,}),
 ]
