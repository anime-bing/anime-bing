from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post,Comment
from django.views.generic import (DetailView,CreateView,ListView,UpdateView,DeleteView)
from .forms import PostEditForm,CommentForm,PostCreateForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.utils.text import slugify
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
# Create your views here.



def postlist(request):
    posts = Post.objects.all().order_by('-created_at')
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query)|Q(author__username=query)|
            Q(description__icontains=query)|Q(content__icontains=query)
        )
    paginator = Paginator(posts,15)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts':posts}
    return render(request,'blog/home.html',context)

# class PostDetailView(DetailView):
#     model = Post


def Post_detail(request,id,slug):
    post = get_object_or_404(Post,id=id,slug=slug)
    if request.method =='POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs=None;
            if reply_id:
                comment_qs = Comment.objects.get(id = reply_id)
            comment = Comment.objects.create(post = post , user = request.user , content = content, reply = comment_qs)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()
    comments  = Comment.objects.filter(post = post , reply=None).order_by('-id')
    context = {
        'post':post ,
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request,'blog/post_detail.html',context)


class CreatePost(LoginRequiredMixin,CreateView):
    model = Post
    # fields = ('title','description','content','post_image')
    form_class = PostCreateForm

    def form_valid(self,form):
        form.instance.author = self.request.user

        return super().form_valid(form)

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'


    def get_queryset(self):
        user = get_object_or_404(User , username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-created_at')

class PostEdit(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model= Post
    template_name = 'blog/post_edit.html'
    form_class = PostEditForm


    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False
