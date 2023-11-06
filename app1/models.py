from django.db import models
import datetime
# Create your models here.

class Book(models.Model):
    Title=models.CharField(max_length=200)
    Author=models.CharField(max_length=200)
    PublicationDate=models.DateField(default=datetime.date.today)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    
    def is_expensive(self):
        if self.price>50:
            return True
        else:
            return False