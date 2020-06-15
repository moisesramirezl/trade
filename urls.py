from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.views.generic import TemplateView
from stocksList import views as stocksListView
from stocksBalance import views as stocksBalanceView

urlpatterns = [
    path('', TemplateView.as_view(template_name='trade/index.html')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    url(r'^stocksList/$',
        stocksListView.index, name='index'),
    url(r'^stocksBalance/$',
        stocksBalanceView.stocksBalance, name='stocksBalance'),
    url(r'^stocksList/(?P<userId>\d+)/create/$',
        stocksListView.stockCreate, name='stockCreate'),
    url(r'^stocksList/(?P<pk>\d+)/update/$',
        stocksListView.stockUpdate, name='stockUpdate'),
]
