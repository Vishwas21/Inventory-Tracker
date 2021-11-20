from django.urls import path
from inventoryCheck.views import homeView, getData, gridView, getGridData

app_name = 'inventoryCheck'

urlpatterns = [
    path('', homeView),
    path('home/', homeView, name="home"),
    path('grid/', gridView, name="grid"),
    path('getdata/', getData),
    path('getsensordata/', getGridData)
]
