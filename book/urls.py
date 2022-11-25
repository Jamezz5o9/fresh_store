from django.urls import path
from . import views
from . import old_views


# urlpatterns = [
#     path("", views.index, name="book-list"),
#     path("<int:pk>/", views.publisher_details, name="publisher-details"),
#     path("<int:uk>/", views.author_details, name="author_details"),
#     path("blog_author/", views.author, name="author_list"),
#     path("books/", views.book_list, name="books-book-list"),
#     path("book-create/", views.book_create, name="book-create"),
# ]


urlpatterns = [
    path("books/", views.book_list, name="book-list"),
    path("books/<int:pk>", views.book_detail, name="book-detail"),
    path("publisher", views.publisher_list, name="publisher-list"),
    path("publisher/<int:pk>", views.publisher_details, name="publisher-details")
]

