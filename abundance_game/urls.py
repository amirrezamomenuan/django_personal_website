"""abundance_game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page_view, name= "home"),
    path('game/', include('game.urls'), name = 'game'),
    path('accounts/', include('accounts.urls'), name = 'accounts'),
    path('confidence/', include('confidence.urls'), name= 'confidence'),
    path('books/', include('books.urls'), name='books')
    # a path to list of my professional goals
]

urlpatterns += staticfiles_urlpatterns()