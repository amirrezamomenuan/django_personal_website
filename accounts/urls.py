from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signin/", views.signin_view, name= "signin"),
    path("login/", views.login_view, name= "login"),
]