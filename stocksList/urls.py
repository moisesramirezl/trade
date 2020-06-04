from django.urls import path

from . import views
app_name = 'stocksList'

urlpatterns = [
    # ex: /stocksList/
    path('', views.index, name='index'),
]
