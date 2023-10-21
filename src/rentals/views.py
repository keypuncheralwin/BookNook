from django.shortcuts import render

# Create your views here.

def search_book_view(request):
    context = {}
    return render(request, 'rentals/main.html', context)
