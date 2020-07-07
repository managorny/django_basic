from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from basketapp.models import Basket
from mainapp.models import Product


def add_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = request.user.basket_set.filter(product=pk).first()
    # basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
