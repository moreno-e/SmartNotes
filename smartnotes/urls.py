"""smartnotes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from home import views
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # DEPENDENCY!
    # path('home', views.home) removed our previous dependency
    
    # rather than passing a function we are passing the file as a string
    # now if the home app gets deleted we safely avoid errors
    path('', include('home.urls')),
    
    # all the notes.urls will not be added after smart
    path('smart/', include('notes.urls')),
]