from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField()
    authors = models.ManyToManyField("Author", related_name="books")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("publisher-details", args=[self.id])


class Book(models.Model):
    GENRE_CHOICES = (
        ("C", "Comedy"),
        ("T", "Tragedy"),
        ("TC", "Tragicomedy"),
        ("CR", "Crime"),
        ("R", "Romance"),
        ("SF", "Science Fiction")
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True)
    isbn = models.CharField(max_length=20)
    date_published = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)
    edition = models.PositiveSmallIntegerField()
    genre = models.CharField(max_length=2, choices=GENRE_CHOICES, default="R")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} ({self.price})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['title']
        db_table = ""


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("author_details", kwargs={"slug": self.slug})


class Address(models.Model):
    number = models.PositiveIntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=6, validators=[MinLengthValidator(5, "code cannot be less than a length 5"),
                                                         MaxLengthValidator(5, "code can only be length of 5")])
    publisher = models.OneToOneField(Publisher, on_delete=models.CASCADE)
