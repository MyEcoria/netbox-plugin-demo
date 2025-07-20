from django.urls import path
from .views import AccessListCounterView

urlpatterns = [
    path('counter/', AccessListCounterView.as_view(), name='counter'),
]
