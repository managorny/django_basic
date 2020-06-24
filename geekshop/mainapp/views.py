from django.shortcuts import render
import json


def index(request):
    context = {
        'page_title': 'Interior',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'page_title': 'Products',
    }
    return render(request, 'mainapp/product-details.html', context)


def contacts(request):
    with open('locations.json', 'r', encoding="utf-8") as file:
        locations = json.load(file)

    context = {
        'page_title': 'Contacts',
        'locations': locations,
    }

    return render(request, 'mainapp/contacts.html', context)
