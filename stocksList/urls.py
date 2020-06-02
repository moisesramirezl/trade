from django.urls import path

from . import views
app_name = 'stocksList'

urlpatterns = [
    # ex: /stocksList/
    path('', views.index, name='index'),
    # ex: /stocksList/5/
    path('<str:user_id>/', views.userStockDetail, name='userStockDetail'),
    # ex: /stocksList/5/results/
    path('<str:user_id>/userStockInfo/',
         views.userStockInfo, name='userStockInfo'),
]
