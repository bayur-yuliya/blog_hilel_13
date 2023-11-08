import time

from django.core.cache import cache
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from posts.forms import PostForm
from posts.models import Post


def posts(request):
    all_posts = Post.objects.all()

    data = {"posts": all_posts}
    return render(request, "posts/all_post.html", data)


def get_post(request, post_id):
    post = cache.get(f'post-{post_id}')
    if not post:
        time.sleep(5)
        post = get_object_or_404(Post, id=post_id)
        cache.set(f'post-{post_id}', post, 60 * 15)
    data = {"post": post}
    return render(request, "posts/post.html", data)


def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "GET":
        form = PostForm(instance=post)
        return render(request, "posts/update_post.html", {'form': form})

    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        form.save()
    cache.delete(f'post-{post_id}')
    return redirect(reverse('post', args=[post_id]))
