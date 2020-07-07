from django.shortcuts import render, get_object_or_404
import json
from mainapp.models import ProductCategory, Product


def index(request):
    context = {
        'page_title': 'Interior',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    categories = ProductCategory.objects.all()
    products_list = Product.objects.all()

    context = {
        'page_title': 'Products',
        'categories': categories,
        'products': products_list[:3],
    }
    return render(request, 'mainapp/product-details.html', context)


def category_products(request, pk):
    categories = ProductCategory.objects.all()

    if pk == '0':
        category = {'pk': 0, 'name': 'Все'}
        products_list_category = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products_list_category = category.product_set.all()

    context = {
        'page_title': 'Products',
        'categories': categories,
        'products': products_list_category,
        'category': category,
    }
    return render(request, 'mainapp/category_products.html', context)


def contacts(request):
    with open('locations.json', 'r', encoding="utf-8") as file:
        locations = json.load(file)

    context = {
        'page_title': 'Contacts',
        'locations': locations,
    }

    return render(request, 'mainapp/contacts.html', context)
