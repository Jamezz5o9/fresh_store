from decimal import Decimal

from rest_framework import serializers

from book.models import Publisher, Book


class PublisherSerializer(serializers.ModelSerializer):  # noqa
    number_of_books_published = serializers.IntegerField(read_only=True)

    class Meta:
        model = Publisher
        fields = ['id', 'name', 'email', 'website', 'number_of_books_published']


# class BookCreateSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#
#     class Meta:
#         model = Book
#         fields = ['id', 'title', 'isbn', 'genre' 'price', 'date_published', 'edition', 'publisher']


class BookSerializer(serializers.ModelSerializer):  # noqa
    # title = serializers.CharField(max_length=255)
    # isbn = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2)
    # publisher = serializers.HyperlinkedRelatedField(
    #     queryset=Publisher.objects.all(),
    #     view_name="publisher-details"
    # )
    # publisher = serializers.StringRelatedField()
    # publisher = serializers.PrimaryKeyRelatedField(
    #     queryset=Publisher.objects.all()
    # )
    # publisher = PublisherSerializer()
    # publisher = serializers.HyperlinkedRelatedField(queryset=Publisher.objects.all(), view_name='publisher-details', )

    # I will use the annotation to add discount to the fields in publisher
    # discounted_price = serializers.SerializerMethodField(method_name="discount", read_only=True)
    #
    # def discount(self, book):
    #     return book.price * Decimal("0.8")

    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'date_published', 'price', 'edition', 'genre', 'publisher']
        # fields = '__all__'
