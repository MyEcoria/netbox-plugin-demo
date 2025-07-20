from django.shortcuts import render, redirect
from django.views import View
from .models import AccessListCounter
from .forms import AccessListCounterForm

class AccessListCounterView(View):
    def get(self, request):
        counter, created = AccessListCounter.objects.get_or_create(name="default")
        return render(request, 'netbox_access_lists/counter.html', {'counter': counter})

    def post(self, request):
        counter, created = AccessListCounter.objects.get_or_create(name="default")
        counter.value += 1
        counter.save()
        return redirect('plugins:netbox_access_lists:counter')
