from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # path('register/', views.register, name='register'),
    path('register/', views.RegisterView.as_view(), name='register'),
    # path('logout/', views.log_out, name='logout'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
]
