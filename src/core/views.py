from django.shortcuts import render


def home_view(request):
    value = 'test value'
    return render(request, 'main.html', {'test_value': value})
