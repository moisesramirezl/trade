from django.db import models

class Nemos(models.Model):
    id = models.AutoField(primary_key=True)
    nemo = models.CharField(max_length=200)
    def __str__(self):
        return self.nemo

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    def __str__(self):
        return self.username

class UserStocks(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT, primary_key=True, unique=True)
    nemo_id = models.ForeignKey(Nemos, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price =  models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    purchase_date = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now=True)