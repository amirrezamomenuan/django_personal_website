from django.db import models
from datetime import date
from accounts.models import User

class Book(models.Model):

    BOOK_STATUS = (
        ('r', 'read'),
        ('t', 'to_be_read'),
    )

    name = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    status = models.CharField(max_length=1, choices=BOOK_STATUS, default='t')
    target = models.DateField()
    times_read = models.SmallIntegerField(default=0)
    reader = models.ForeignKey(User, models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.name
    
    def change_status(self):
        if self.status == 'r':
            self.status = 't'
        elif self.status == 't':
            self.status = 'r'
            self.times_read += 1
        self.save()
    
    def days_left(self):
        today = date.today()
        return (self.target - today).days
    
    def set_target(self,dateinput):
        self.target = dateinput
        self.save()