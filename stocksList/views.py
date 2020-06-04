from django.http import HttpResponse
from django.template import loader
from .models import StocksList
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    stocksList = StocksList.objects
    template = loader.get_template('stocksList/index.html')
    context = {
        'stocksList': stocksList,
    }
    return HttpResponse(template.render(context, request))
