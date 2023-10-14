from django.shortcuts import render
from customers.models import Customer


def home_view(request):
    qs = Customer.objects.all()
    return render(request, 'main.html', {'qs': qs})
