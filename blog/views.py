from django.shortcuts import render,get_object_or_404, redirect, HttpResponseRedirect ,reverse
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()

    return render(request, 'blog/post_list.html', {
        'post_list': posts
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {
        'post': post
    })


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')

    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {
        'form': form
    })


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')

    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {
        'form': form
    })
