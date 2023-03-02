from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from . models import Post
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django .views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']  


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs['username'])
        return Post.objects.filter(author = user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, SuccessMessageMixin ,CreateView):
    model = Post
    fields = ['title', 'content']
    success_message = 'Post Has been created successfully!'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # Template name will be modelname_form as it shares template with postupdateview

class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_message = 'Post Has been updated successfully!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


# Post Delete view is similar to Detail View
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,SuccessMessageMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('blog-home')
    success_message = 'Post Has been deleted Successfully!!'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    return render(request, 'blog/about.html')

