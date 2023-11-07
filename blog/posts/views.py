from django.shortcuts import render, get_object_or_404

from posts.models import Post


def get_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    data = {"post": post}
    return render(request, "posts/post.html", data)


def posts(request):
    posts = Post.objects.all()
    data = {"posts": posts}
    return render(request, "posts/all_post.html", data)
