from django.urls import path
from . import views

app_name = 'confidence'

urlpatterns = [
    path('add/', views.add_view, name='add'),
    path('list/', views.list_view, name='list'),
    path('todays-adds/', views.todays_adds_view),
]