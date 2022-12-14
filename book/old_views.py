from django.db.models import Count, Avg, Q, F, ExpressionWrapper, DecimalField
from django.shortcuts import render, get_object_or_404
from .models import Publisher, Author, Book
from .forms import BookForm


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
    authors = get_object_or_404(Author, uk=uk)
    return render(request, "book/author_details.html", context={"author": authors})


def book_list(request):
    # queryset = Book.objects.all()
    # queryset = Book.objects.select_related('publisher').all()
    # queryset = Book.objects.select_related('publisher').filter(title__icontains='the').filter(price__gt=100)
    # queryset = Book.objects.select_related('publisher').filter(Q(title__icontains='the') | Q(price__isnull=True))
    # queryset = Book.objects.select_related('publisher').filter(title=F('slug'))
    queryset = Book.objects.select_related('publisher').filter(title=F('slug')).annotate(
        discounted_price=ExpressionWrapper(F('price') * 0.8, output_field=DecimalField()))
    result = queryset.aggregate(count=Count('id'), average=Avg('price'))
    return render(request, "book/book-list.html", context={"books": list(queryset), "result": result})


def book_create(request):

    form = BookForm()

    if request.method == "POST":
        print(request.POST)
        form = BookForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        return render(request, "book/book-create.html", context={"form": form})

    else:
        return render(request, "book/book-create.html", context={"form": form})

