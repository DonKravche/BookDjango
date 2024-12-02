from django.urls import path
from . import views

app_name = 'Book'

urlpatterns = [
    path('', views.index, name='index'),
    ###
    path('index-cbv/', views.IndexView.as_view(), name='index-cbv'),
    path('book-cbv/detail/<int:pk>/', views.BookDetailView.as_view(), name='book-cbv-detail'),
    path('book-cbv/add/', views.AddBookView.as_view(), name='book-cbv-add'),

    path('book/add', views.addBook, name='book_add'),
    path('book/detail/<int:pk>', views.book_detail, name='book_detail'),
]