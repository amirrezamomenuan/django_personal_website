from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import datetime
from game import forms
from . import forms
from django.contrib.auth.decorators import login_required
from .models import Transaction, Game

@login_required(login_url= '/accounts/login')
def spend_view(request):

    if not hasattr(request.user, 'game'):
        # print('fuck you')
        return redirect('game_root_name:create')


    # print(request.method)
    if request.method == "POST":
        form = forms.transaction_form(request.POST)
        # print('got_form\n')
        if form.is_valid():
            game = Game.objects.get(player = request.user)

            if form.cleaned_data['amount'] > game.todays_amount:
                return HttpResponse('sorry you will have more money tommorow :)')

            transaction = form.save(commit=False)
            transaction.owner = request.user
            transaction.save()

            game.todays_amount -= form.cleaned_data.get('amount')
            game.save()
            return redirect("game_root_name:game-day", str(datetime.date.today()))
        else:
            print("form errors:\n")
            # print(form.errors())

    form = forms.transaction_form()
    return render(request, 'spend.html', {'form':form})

@login_required(login_url= '/accounts/login')
def transaction_view(request, id):
    transaction = Transaction.objects.get(id = id)
    if request.user != transaction.owner:
        return HttpResponse("sorry! transaction not found")
    return HttpResponse(transaction.description)


@login_required(login_url= '/accounts/login')
def game_day_view(request, date):
    todays_transactions = Transaction.objects.filter(date = date, owner = request.user).order_by('-time')
    return render(request, 'todays_transactions.html', {"todays_transactions":todays_transactions})


@login_required(login_url= '/accounts/login')
def game_day_list_view(request):
    pass


@login_required(login_url= '/accounts/login')
def main_game_view(request):
    
    if hasattr(request.user, 'game'):
        return redirect('game_root_name:spend')
        
    user = request.user
    Game.objects.create(player = user)
    return redirect('game_root_name:spend')