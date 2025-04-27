from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product
from catalog.forms import ProductForm, ModeratorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'detail_list.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class  = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class  = ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.request.user.has_perm("catalog.can_unpublish_product"):
            return ModeratorForm
        return ProductForm

    def get_change(self, request, *args, **kwargs):
        product = super().get_object()
        if product.owner == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden("Вы не можете изменять этот продукт")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_delete(self, request, *args, **kwargs):
        product = super().get_object()
        if product.owner == self.request.user or self.request.user.has_perm("catalog.can_unpublish_product"):
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden("Вы не можете удалить этот продукт")
