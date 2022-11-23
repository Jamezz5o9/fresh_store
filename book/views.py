from django.shortcuts import render, get_object_or_404
from .models import Publisher, Author


# Create your views here.git

def index(request):
    # queryset = Publisher.objects.filter(website__startswith="http")
    # queryset = Publisher.objects.filter(id__range=(1, 5))
    # queryset = Publisher.objects.filter(id__range=(5, 8))
    # queryset = Publisher.objects.all()
    # queryset = Publisher.objects.filter(name="Skinder")
    # queryset = Publisher.objects.filter(id__range=(1, 3))
    queryset = Publisher.objects.filter(website__startswith="http")
    return render(request, "book/index.html", context={"publishers": list(queryset)})


# def publisher_list(request):
#     queryset = Publisher.objects.all()

def publisher_details(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    return render(request, "book/publisher-details.html", context={"publisher": publisher})


def author(request):
    queryset = Author.objects.all()
    return render(request, "book/author_index.html", context={"author": queryset})


def author_details(request, uk):
    author = get_object_or_404(Author, uk=uk)
    return render(request, "book/author_details.html", context={"author": author})
