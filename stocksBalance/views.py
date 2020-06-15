from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Nemos


@login_required
def stocksBalance(request):
    allNemosAbailavle = Nemos.objects.using(
        'historical-nemos').values('nemo').distinct()

    lastNemosPrice = {}

    for nemo in allNemosAbailavle:
        getObj = Nemos.objects.using(
            'historical-nemos').filter(nemo=nemo.get('nemo')).order_by('-registerdatetime')[0]
        lastNemosPrice[nemo.get('nemo')] = getObj.lastprice

    return render(request, 'stocksBalance/stocksBalance.html', {"nemos": lastNemosPrice})
