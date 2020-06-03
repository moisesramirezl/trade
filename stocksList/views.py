from django.http import HttpResponse
from django.template import loader
from .models import StocksList
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    latest_stocks_list = StocksList.objects.order_by('-timestamp')[:5]
    template = loader.get_template('stocksList/index.html')
    context = {
        'latest_stocks_list': latest_stocks_list,
    }
    return HttpResponse(template.render(context, request))


def userStockDetail(request, user_id):
    return HttpResponse("You're looking at user_id %s." % user_id)


def userStockInfo(request, user_id):
    response = "You're looking the info of user_id %s."
    return HttpResponse(response % user_id)
