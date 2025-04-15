from django.urls import path
from catalog.apps import CatalogConfig
from .views import ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail_list'),
]
