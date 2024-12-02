from django.urls import path

from . import views

app_name = "orders"

urlpatterns = [
    path("cart/", views.cart_view, name="cart_view"),
    # path("cart/add/<int:pk>", views.add_cart_item, name="add_cart_item"),

    path("cart/add/<int:pk>", views.AddCartItemView.as_view(), name="add_cart_item"),
    # path("cart/update/<int:pk>", views.update_cart_item, name="update_cart_item"),
    path("cart/update/<int:pk>", views.UpdateCartItemView.as_view(), name="update_cart_item"),

    # path("cart/delete/<int:pk>", views.delete_cart_item, name="delete_cart_item"),

    path("cart/delete/<int:pk>", views.DeleteCartItemView.as_view(), name="delete_cart_item"),

    path("processes_to_check_out/", views.processes_to_check_out, name="processes_to_check_out"),
    path("confirm/<int:order_id>/", views.confirm_order, name="confirm_order"),
    path("past-orders/", views.past_orders, name="past_orders"),
]
