from django.urls import path
from . views import BookDetailView, BookTitleListView, BookTitleDetailView, BookDeleteView

app_name = 'books'

urlpatterns = [
    path('', BookTitleListView.as_view(), {'letter':''}, name='main'),
    path('<str:letter>/', BookTitleListView.as_view(), name='main'),
    path('<str:letter>/<slug>/', BookTitleDetailView.as_view(), name='detail'),
    path('<str:letter>/<slug>/<str:book_id>/', BookDetailView.as_view(), name='detail-book'),
    path('<str:letter>/<slug>/<str:book_id>/delete', BookDeleteView.as_view(), name='delete-book'),
]
