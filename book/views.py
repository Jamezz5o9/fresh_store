from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer, PublisherSerializer
from .models import Book, Publisher


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        queryset = Book.objects.select_related('publisher').all()
        serializer = BookSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        serializer = BookSerializer(book, context={"request": request})
        return Response(serializer.data)
    elif request.method in ('PUT', 'PATCH'):
        serializer = BookSerializer(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def publisher_list(request):
    if request.method == "GET":

        queryset = Publisher.objects.annotate(
            number_of_books_published=Count('books')
        ).all()
        serializer = PublisherSerializer(queryset, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PublisherSerializer(dat=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view()
def publisher_details(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    serializer = PublisherSerializer(publisher)
    return Response(serializer.data)
