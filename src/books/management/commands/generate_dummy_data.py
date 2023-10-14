from django.core.management.base import BaseCommand
from authors.models import Author
from publishers.models import Publisher
from books.models import BookTitle, Book
from customers.models import Customer
from django_countries.fields import Country
import random


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # generating authors

        authors_list = ["Alice Johnson", "Brian Smith",
                        "Charlotte Brown", "David White", "Emily Miller"]
        for name in authors_list:
            Author.objects.create(name=name)

        # generating publishers

        publishers_list = [
            {'name': 'x books', 'country': Country(code='us')},
            {'name': 'Another Book', 'country': Country(code='de')},
            {'name': 'Random Book', 'country': Country(code='gb')}
        ]

        for item in publishers_list:
            Publisher.objects.create(**item)

        # generating book titles

        book_title_list = ["Whispers of the Silent Ocean", "The Last Clockmaker's Dream", "Through the Emerald Gateway",
                           "Chronicles of the Forgotten Kingdom", "The Enchanted Tapestry"]
        publishers = [x.name for x in Publisher.objects.all]
        items = zip(book_title_list, publishers)

        for item in items:
            author = Author.objects.order('?')[0]
            publisher = Publisher.objects.get(name=item[1])
            BookTitle.objects.create(
                title=item[0], publisher=publisher, author=author)

        # generating books

        book_titles = BookTitle.objects.all()

        for title in book_titles:
            quantity = random.randint(1, 5)
            for i in range(quantity):
                Book.objects.create(title=title)

        # generating custoemrs

        customers_list = [
            {'first_name': 'John', 'last_name': 'Doe'},
            {'first_name': 'Jane', 'last_name': 'Smith'},
            {'first_name': 'Alice', 'last_name': 'Johnson'},
            {'first_name': 'Bob', 'last_name': 'Brown'},
            {'first_name': 'Charlie', 'last_name': 'White'}]

        for item in customers_list:
            Customer.objects.create(**item)
