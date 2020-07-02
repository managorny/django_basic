from django.urls import path, re_path

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    re_path(r'add/product/(?P<pk>\d+)/', basketapp.add_product, name="add_product"),
    # path('add/product/<int:pk>'/, basketapp.add_product, name="add_product"),
]
