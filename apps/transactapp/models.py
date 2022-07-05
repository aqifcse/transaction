from unicodedata import name
from django.db import models
from django.utils.timezone import now

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    sent_from = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_to = models.ManyToManyField(User, related_name='sent_to')
    sent_at = models.DateTimeField(default=now)
    amount_sent = models.FloatField()
