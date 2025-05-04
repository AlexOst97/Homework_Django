from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogsListView, BlogsCreateView, BlogsDetailView, BlogsUpdateView, BlogsDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/', BlogsListView.as_view(), name='blogs_list'),
    path('blog/create/', BlogsCreateView.as_view(), name='blogs_create'),
    path('blog/<int:pk>/', BlogsDetailView.as_view(), name='blogs_detail'),
    path('blog/<int:pk>/update/', BlogsUpdateView.as_view(), name='blogs_update'),
    path('blog/<int:pk>/delete/', BlogsDeleteView.as_view(), name='blogs_delete'),
]