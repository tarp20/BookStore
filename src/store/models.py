from django.db import models
from django.contrib.auth.models import User

from store.func import set_rating


class Book(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(
        decimal_places=2, 
        max_digits=5)
    author_name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='my_books')
    reader = models.ManyToManyField(
        User, 
        through='UserBookRelation', 
        related_name='books')
    
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=None,
        null=True)

    def __str__(self):
        return self.name


class UserBookRelation(models.Model):
    RATE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE)
    like = models.BooleanField(
        default=False,
        null=True)
    is_bookmark = models.BooleanField(default=False)
    rate = models.PositiveIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return f'{self.user.username}: {self.book.name}'

    def save(self,*args, **kwargs):
        from store.func import set_rating
        creating = not self.pk
        old_rating = self.rate
        super().save(*args, **kwargs)
        new_rating = self.rate
        if old_rating != new_rating or creating:
            set_rating(self.book)
