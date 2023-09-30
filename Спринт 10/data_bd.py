import csv

# from django.conf import settings
from django.core.management import BaseCommand
from reviews.models import (
    Category, Comment, Genre, GenreTitle, Review, Title, User)

TABLES_DICT = {
    User: 'users.csv',
    Category: 'category.csv',
    Genre: 'genre.csv',
    Title: 'titles.csv',
    Review: 'review.csv',
    Comment: 'comments.csv',
    GenreTitle: 'genre_title.csv'
}


# class Command(BaseCommand):
#     help = 'Load csv data'

#     def handle(self, *args, **kwargs):
#         for model, base in TABLES_DICT.items():
#             with open(
#                 f'{settings.BASE_DIR}/static/data/{base}',
#                 'r', encoding='UTF-8'
#             ) as csv_file:
#                 reader = csv.DictReader(csv_file)
#                 model.objects.bulk_create(model(**data) for data in reader)

#         self.stdout.write(self.style.SUCCESS('Successfully'))
class Command(BaseCommand):
    help = 'Loading data from csv to DB'

    def handle(self, *args, **options):
        with open('static/data/category.csv', encoding='UTF-8') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                id, name, slug = row
                if name != 'name':
                    Category.objects.get_or_create(name=name, slug=slug)

        with open('static/data/genre.csv', encoding='UTF-8') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                id, name, slug = row
                if name != 'name':
                    Genre.objects.get_or_create(name=name, slug=slug)

        with open('static/data/genre.csv', encoding='UTF-8') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                id, name, slug = row
                if name != 'name':
                    User.objects.get_or_create(name=name, slug=slug)

        with open('static/data/genre.csv', encoding='UTF-8') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                id, name, slug = row
                if name != 'name':
                    Title.objects.get_or_create(name=name, slug=slug)

        with open('static/data/genre.csv', encoding='UTF-8') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                id, name, slug = row
                if name != 'name':
                    Comment.objects.get_or_create(name=name, slug=slug)

        with open('static/data/genre.csv', encoding='UTF-8') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                id, name, slug = row
                if name != 'name':
                    Review.objects.get_or_create(name=name, slug=slug)
