from django.db import models
from datetime import datetime

# Create your models here.

class Record(models.Model):
    name = models.CharField(max_length=30, unique=True)
    creation_date = models.DateTimeField(default=datetime.now())
    number = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email


class History(models.Model):
    name = models.ForeignKey(Record, on_delete=models.CASCADE)
    loan_amount = models.IntegerField()
    percentage = models.IntegerField()


    def interest(self):
        return self.loan_amount * self.percentage / 100

    def time(self):
        return self.loan_amount / self.interest()

    def __str__(self):
        return self.name.name