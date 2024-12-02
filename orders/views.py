from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404

from Book.models import Book
from .models import Cart, CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import View, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


@login_required(login_url='/users/login')
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    total_amount = sum(cart_item.total for cart_item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_amount': total_amount})


@login_required(login_url='/users/login')
def add_cart_item(request, pk):
    book = Book.objects.get(pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)
    # print(f'Book: {pk}', book.stock)
    if book.stock > 0:
        cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, book=book)
        # print(f'CartItem: {cart_item.book.title}', cart_item_created)
        if not cart_item_created:
            cart_item.quantity += 1
        else:
            cart_item.quantity = 1
        cart_item.save()
        # print("SAVED!")

    return redirect(request.META['HTTP_REFERER'])


class AddCartItemView(View):
    @staticmethod
    def get(request, pk):
        book = Book.objects.get(pk=pk)

        cart, created = Cart.objects.get_or_create(user=request.user)
        # print(f'Book: {pk}', book.stock)
        if book.stock > 0:
            cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, book=book)
            # print(f'CartItem: {cart_item.book.title}', cart_item_created)
            if not cart_item_created:
                cart_item.quantity += 1
            else:
                cart_item.quantity = 1
            cart_item.save()
            # print("SAVED!")

        return redirect('orders:cart_view')


@login_required(login_url='/users/login')
def update_cart_item(request, pk):
    if request.method == 'POST':
        cart_item = CartItem.objects.get(pk=pk)

        new_quantity = int(request.POST.get('quantity'))

        if new_quantity == 0:
            cart_item.delete()

        elif new_quantity < cart_item.book.stock:
            cart_item.quantity = new_quantity
            cart_item.save()

    return redirect(request.META['HTTP_REFERER'])


class UpdateCartItemView(View):
    @staticmethod
    def post(request, pk):
        cart_item = CartItem.objects.get(pk=pk)

        new_quantity = int(request.POST.get('quantity'))

        if new_quantity == 0:
            cart_item.delete()

        elif new_quantity < cart_item.book.stock:
            cart_item.quantity = new_quantity
            cart_item.save()

        return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='/users/login')
def delete_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk)

    cart_item.delete()
    return redirect(request.META['HTTP_REFERER'])


class DeleteCartItemView(DeleteView):
    model = CartItem
    success_url = reverse_lazy('orders:cart_view')




@login_required(login_url='/users/login')
def processes_to_check_out(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    if not cart_items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect('orders:cart_view')

    total_amount = sum(cart_item.total for cart_item in cart_items)
    order = Order.objects.create(user=request.user, cart=cart)

    order_items = [
        OrderItem.objects.create(
            order=order,
            book=cart_item.book,
            quantity=cart_item.quantity
        ) for cart_item in cart_items
    ]

    cart_items.delete()

    return render(request, 'processes_to_check_out.html', {
        'order_items': order_items,
        'total_amount': total_amount,
        'order': order
    })


@login_required(login_url='/users/login')
def confirm_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.orderitem_set.all()

    # Update book stock
    for item in order_items:
        book = item.book
        book.stock -= item.quantity
        book.save()

    # Clear user's cart
    Cart.objects.filter(user=request.user).delete()

    # Add a success message
    messages.success(request, "Order confirmed successfully!")

    # Redirect to index page
    return redirect('Book:index')


@login_required(login_url='/users/login')
def past_orders(request):
    # Get all orders for the current user, ordered by most recent first
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    # Prepare a list of orders with their total amounts
    order_details = []
    for order in orders:
        order_items = order.orderitem_set.all()
        total_amount = sum(item.book.price * item.quantity for item in order_items)
        order_details.append({
            'order': order,
            'items': order_items,
            'total_amount': total_amount
        })

    return render(request, 'past_orders.html', {
        'order_details': order_details
    })
