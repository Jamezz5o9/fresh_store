from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import old_views

# urlpatterns = [
#     path("", views.index, name="book-list"),
#     path("<int:pk>/", views.publisher_details, name="publisher-details"),
#     path("<int:uk>/", views.author_details, name="author_details"),
#     path("blog_author/", views.author, name="author_list"),
#     path("books/", views.book_list, name="books-book-list"),
#     path("book-create/", views.book_create, name="book-create"),
# ]


router = DefaultRouter()
router.register('books', viewset=views.BookViewSet, basename='book')
router.register('publisher', viewset=views.PublisherViewSet, basename='publisher')

urlpatterns = [
    path('', include(router.urls)),
    # path("books/", views.book_list, name="book-list"),
    # path("books/", views.BookList.as_view(), name="book-list"),
    # # path("books/<int:pk>", views.book_detail, name="book-detail"),
    # path("books/<int:pk>", views.BookDetail.as_view(), name="book-detail"),
    # path("publisher", views.publisher_list, name="publisher-list"),
    # path("publisher", views.PublisherList.as_view(), name="publisher-list"),
    # path("publisher/<int:pk>", views.publisher_details, name="publisher-details")
    # path("publisher/<int:pk>", views.PublisherDetails.as_view(), name="publisher-details")
]
