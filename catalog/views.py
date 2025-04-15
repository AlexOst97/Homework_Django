from django.views.generic import ListView, DetailView
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail_list.html'
    context_object_name = 'product'