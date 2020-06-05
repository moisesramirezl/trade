from django import forms
from .models import StocksList


class StocksListForm(forms.ModelForm):
    class Meta:
        model = StocksList
        fields = ('nemo', 'quantity', 'purchasePrice',
                  'saleTargetPrice', 'tax', 'purchaseDate')
