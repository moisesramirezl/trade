from django.db import models
from django.contrib.auth.models import User


class StocksList(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="stocksList", null=True)
    nemo = models.CharField(max_length=200)
    quantity = models.IntegerField()
    purchasePrice = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    saleTargetPrice = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    purchaseDate = models.DateField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nemo
