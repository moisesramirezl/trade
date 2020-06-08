from django import forms
from .models import StocksList
from django.contrib.auth.models import User


class StocksListForm(forms.ModelForm):
    class Meta:
        model = StocksList
        fields = ('user', 'nemo', 'quantity', 'purchasePrice',
                  'saleTargetPrice', 'tax', 'purchaseDate')
