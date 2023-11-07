from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from posts.models import Post


@cache_page(60 * 15)
def get_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    data = {"post": post}
    return render(request, "posts/post.html", data)


@cache_page(60 * 15)
def posts(request):
    all_posts = Post.objects.all()
    data = {"posts": all_posts}
    return render(request, "posts/all_post.html", data)
