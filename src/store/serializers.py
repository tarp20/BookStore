from rest_framework import serializers


from .models import Book, UserBookRelation


class BookSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(read_only=True)
    rating = serializers.DecimalField(read_only=True,max_digits=3,decimal_places=1)
    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'author_name','like_count', 'rating')


class UserBookRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ('book', 'like', 'is_bookmark', 'rate')
