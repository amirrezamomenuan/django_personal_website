from django.db import models
from accounts.models import User

class GreateJob(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.CharField(max_length=128)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner.first_name} => {self.job[:30]}'