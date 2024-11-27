from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    category_type = models.CharField(max_length=100, default='General')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=50)
    pages = models.IntegerField()
    publish_date = models.DateField()
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.title
