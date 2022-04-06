from django.urls import path
from . import views

app_name = 'game_root_name'

urlpatterns = [
    path('spend/', views.spend_view, name ='spend'),
    path('transaction/<int:id>', views.transaction_view, name = 'transaction'),
    path('game-day/<date>', views.game_day_view, name = 'game-day'),
    path('game-days/', views.game_day_list_view),
    path('', views.main_game_view, name='create'),
]