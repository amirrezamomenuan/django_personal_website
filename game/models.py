from django.db import models
from accounts.models import User



class Transaction(models.Model):
    amount = models.PositiveBigIntegerField()
    title = models.CharField(null = True, blank=True, max_length=64)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(null=True, blank=True, auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "transaction")

    def __str__(self):
        return f"expence at:{self.date}, amount:{self.amount}"
        
    def show_title(self):
        return f"{self.title} : {self.amount}"

User.groups.related_name = 'userrelatedname'


class Game(models.Model):
    STATUS_CHOICES = (
        ("n", 'next_day'),
        ('l', 'lost')
    )

    day = models.SmallIntegerField(default=1)
    player = models.OneToOneField(User, on_delete=models.CASCADE, related_name='game')
    todays_amount = models.IntegerField(default=10000)
    game_status = models.CharField(max_length=5, choices=STATUS_CHOICES, default="n")

    def __str__(self):
        return self.player.username + "'s game"