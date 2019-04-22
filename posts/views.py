from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, reverse, Http404
from .forms import PostForm as BlogForm, CommentForm
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .decorator import is_post


# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 6)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)

    context = {'posts': posts}
    return render(request, 'posts/post-list.html', context)


@login_required
def post_create(request):
    if request.user.username == 'selametsamli' or request.user.username == 'hizirsamli':
        form = BlogForm()
        if request.method == 'POST':
            # print(request.POST)
            form = BlogForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                blog = form.save(commit=False)
                blog.user = request.user
                blog.save()
                msg = 'Tebrikler <strong> %s </strong> isimli gönderiniz başarı ile oluşturuldu.' % (blog.title)
                messages.success(request, msg, extra_tags='success')

                return HttpResponseRedirect(blog.get_absolute_url())  # post detail sayfasına yönlendirir.
        return render(request, 'posts/post-create.html', context={'form': form})
    raise Http404

@login_required(login_url=reverse_lazy('user-login'))
def post_detail(request, slug):
    form = CommentForm()
    blog = get_object_or_404(Post, slug=slug)
    # print(blog.get_blog_comment())

    return render(request, 'posts/post-detail.html', context={'blog': blog, 'form': form})


@login_required(login_url=reverse_lazy('user-login'))
def post_update(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    if request.user != blog.user:
        return HttpResponseForbidden
    form = BlogForm(instance=blog, data=request.POST or None,
                    files=request.FILES or None)  # bloğun içerisindeki değerleri çeker
    if form.is_valid():
        form.save()
        msg = 'Tebrikler %s isimli gönderiniz başarı ile güncellendi.' % (blog.title)
        messages.success(request, msg, extra_tags='info')
        return HttpResponseRedirect(blog.get_absolute_url())
    context = {'form': form, 'blog': blog}

    return render(request, 'posts/post-update.html', context)


@login_required(login_url=reverse_lazy('user-login'))
def post_delete(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    if request.user != blog.user:
        return HttpResponseForbidden
    blog.delete()
    msg = 'Tebrikler %s isimli gönderiniz başarı ile silindi.' % (blog.title)
    messages.success(request, msg, extra_tags='danger')

    return HttpResponseRedirect(reverse('post-list'))


@login_required(login_url=reverse_lazy('user-login'))
@is_post
def add_comment(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    form = CommentForm(data=request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.blog = blog
        new_comment.user = request.user
        new_comment.save()
        messages.success(request, 'Tebrikler yorumunuz başarı ile oluşturuldu')
        return HttpResponseRedirect(blog.get_absolute_url())
