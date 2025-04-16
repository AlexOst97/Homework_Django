from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product
from catalog.forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail_list.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class  = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class  = ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('catalog:product_list')