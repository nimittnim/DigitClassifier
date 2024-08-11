from django.urls import path
from .views import home,result, predict

urlpatterns = [
    path('',home, name = 'home'),
    path('result/',result, name = 'result'),
    path('predict/',predict, name = 'predict')
]