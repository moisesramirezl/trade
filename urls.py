from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from stocksList import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='trade/index.html')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('stocksList/', include('stocksList.urls'))
]
