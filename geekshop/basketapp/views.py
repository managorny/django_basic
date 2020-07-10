from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse

from basketapp.models import Basket
from django.urls import reverse
from mainapp.models import Product


@login_required
def index(request):
    context = {
        'basket': request.user.basket.all()
    }
    return render(request, 'basketapp/index.html', context)


@login_required
def add_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = request.user.basket.filter(product=pk).first()
    # basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def delete_product(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    basket.delete()
    return HttpResponseRedirect(reverse('basket:index'))


def change(request, pk, quantity):
    if request.is_ajax():
        print('ajax', pk, quantity)
        return JsonResponse({
            'status': True,
        })
