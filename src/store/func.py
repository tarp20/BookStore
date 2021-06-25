from django.db.models.aggregates import Avg

from .models import UserBookRelation


def set_rating(book):
    rating = UserBookRelation.objects.filter(book=book).aggregate(rating=Avg('rate'))
    book.rating = rating
    book.save()
