"""DEVProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


from DFUApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signin/', views.signIn, name='signin'),
    url(r'^postsign/', views.postsign),
    url(r'^welcome/', views.welcome, name='welcome'),  # delete this url later
    url(r'^logout/', views.logout, name="logout"),
    url(r'^entryform/', views.entryform, name='entryForm'),
    url(r'^post_create/', views.post_create, name='post_create'),

    url(r'^formdata/', views.formdata, name='formData'),
    url(r'^get_data/', views.get_data, name='get_data'),
    url(r'^display_form/', views.display_form, name='display_form'),

    url(r'^imagedata/', views.imagedata, name='imageData'),
    url(r'^downloaddata/', views.downloaddata, name='downloadData'),
    # url(r'^post_download/', views.post_download, name='post_download'),
    url(r'^uploaddata/', views.uploaddata, name='uploadData'),

    url(r'^about/', views.about, name='about'),

    url(r'^post_check/', views.post_check, name='post_check'),
    url(r'^check/', views.check, name='check'),
]
