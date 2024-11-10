from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=50)
    pages = models.IntegerField()
    publish_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.title