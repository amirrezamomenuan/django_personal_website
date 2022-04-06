from tracemalloc import get_object_traceback
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models
from .forms import BookForm, Book
from datetime import date

@login_required(login_url='../../accounts/login')
def read_books_view(request, status):
    if request.method == 'GET':
        books = models.Book.objects.filter(status = status, reader = request.user).order_by('target')
        if status == 'r':
            books =  models.Book.objects.filter(status = status, reader = request.user).order_by('times_read')
        today = date.today()
        var = {'books':books, 'today':today ,'state':status}
        return render(request, 'books.html', var)
    
    elif request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = Book.objects.get(id = book_id)
        book.change_status()
        if request.POST.get('target'):
            date_in = request.POST['target'].split("T")[0].split('-')
            # print(date_in)
            book.set_target(date(int(date_in[0]),int(date_in[1]),int(date_in[2])))
            return redirect('../t')
        return redirect('../r')
    

@login_required(login_url= '../accounts/login')
def add_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.reader = request.user
            form.save()
            return redirect('../t')
        print('form is invalid\n')
    form = BookForm()
    return render(request, 'add_book.html', {'form':form})

@login_required(login_url='../accounts/login')
def delete_book_view(request):
    if request.method == 'POST':
        book = get_object_or_404(Book, id = request.POST.get('pk'))
        if book.reader == request.user:
            book.delete()
            return redirect("books:change" ,status = 't')
        else:
            return HttpResponse('!نمیتونی کتاب های بقیه رو حذف کنی')
    return HttpResponse('!صفحه مورد نظر پیدا نشد')