from django.http import HttpResponse
from django.template import loader
from .models import StocksList
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import StocksListForm
from django.contrib.auth.models import User


@login_required
def index(request):
    stocksList = StocksList.objects
    template = loader.get_template('stocksList/index.html')
    context = {
        'stocksList': stocksList,
    }
    return HttpResponse(template.render(context, request))


def stockCreate(request):
    data = dict()
    if request.method == 'POST':
        form = StocksListForm(request.POST)
        if form.is_valid():
            # TODO Validar que el campo userId del GET es el del usuario logeado
            form.save()
            data['formIsValid'] = True
        else:
            data['formIsValid'] = False
    else:
        form = StocksListForm()

    # TODO Validar que request.GET.get('userId') sea un campo valido para prevenir sql injection
    form.fields['user'].queryset = User.objects.filter(
        id=request.GET.get('userId'))
    context = {'form': form}
    data['htmlForm'] = render_to_string('stocksList/partial_stock_create.html',
                                        context,
                                        request=request,
                                        )
    return JsonResponse(data)
