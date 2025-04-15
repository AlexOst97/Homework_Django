from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import Blogs
from django.urls import reverse_lazy, reverse


class BlogsListView(ListView):
    model = Blogs
    template_name = 'blogs_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blogs.objects.filter(is_active = True)


class BlogsCreateView(CreateView):
    model = Blogs
    fields = ['title', 'contents', 'image', 'is_active']
    template_name = 'blogs_create.html'
    success_url = reverse_lazy('blog:blogs_list')


class BlogsDetailView(DetailView):
    model = Blogs
    template_name = 'blogs_detail.html'
    context_object_name = 'blogs'

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.views += 1
        self.object.save()
        return self.object


class BlogsUpdateView(UpdateView):
    model = Blogs
    fields = ['title', 'contents', 'image', 'is_active']
    template_name = 'blogs_update.html'

    def get_success_url(self):
        return reverse('blog:blogs_detail', kwargs={'pk': self.object.pk})


class BlogsDeleteView(DeleteView):
    model = Blogs
    template_name = 'blogs_delete.html'
    success_url = reverse_lazy('blog:blogs_list')