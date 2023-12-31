from django.shortcuts import render
from home.models import *

def home(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'home.html', context)
