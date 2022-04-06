from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('add/', views.add_book_view, name= 'add'),
    path("delete/", views.delete_book_view, name='delete'),
    path('<str:status>/', views.read_books_view, name='change'),
]