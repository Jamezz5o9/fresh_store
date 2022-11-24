from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
