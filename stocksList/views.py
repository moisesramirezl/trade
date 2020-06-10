from django.http import HttpResponse
from django.template import loader
from .models import StocksList
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import StocksListForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string


@login_required
def index(request):
    stocksList = StocksList.objects
    template = loader.get_template('stocksList/index.html')
    context = {
        'stocksList': stocksList,
    }
    return HttpResponse(template.render(context, request))


def saveStockForm(request, form, templateName, userId):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            # TODO Validar que el campo userId del GET es el del usuario logeado
            form.save()
            data['formIsValid'] = True
            # TODO aca deberia gatillar que se recargue automaticamente la pagina para reflejar los cambios
        else:
            data['formIsValid'] = False

    # TODO Validar que request.GET.get('userId') sea un campo valido para prevenir sql injection
    if(userId is not None):
        form.fields['user'].queryset = User.objects.filter(
            id=userId)
    context = {'form': form}
    data['htmlForm'] = render_to_string(
        templateName, context, request=request)
    return JsonResponse(data)


def stockCreate(request, userId):
    user = get_object_or_404(User, id=userId)
    if request.method == 'POST':
        form = StocksListForm(request.POST)
    else:
        form = StocksListForm(instance=user)
    return saveStockForm(request, form, 'stocksList/partial_stock_create.html', userId)


def stockUpdate(request, pk):
    stock = get_object_or_404(StocksList, pk=pk)
    if request.method == 'POST':
        form = StocksListForm(request.POST, instance=stock)
    else:
        form = StocksListForm(instance=stock)
    return saveStockForm(request, form, 'stocksList/partial_stock_update.html', stock.user_id)
