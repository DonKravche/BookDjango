from django.urls import path
from . import views

app_name = 'Book'

urlpatterns = [
    path('', views.index, name='index'),
    path('book/add', views.addBook, name='book_add'),
    path('book/detail/<int:pk>', views.book_detail, name='book_detail'),
]