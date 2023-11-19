from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from customers.models import Customer
from django.views.generic import TemplateView

def change_theme(request):
    if 'is_dark_mode' in request.session:
        request.session['is_dark_mode'] = not request.session['is_dark_mode']
    else:
        request.session['is_dark_mode'] = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

def chart_data(request):
    return JsonResponse({'msg': 'Test chart data'})