from django.shortcuts import render


def get_post(request, post_id):
    data = {'data': 'data', 'post_id': post_id, 'title': 'title'}
    return render(request, 'posts/post.html', data)


def posts(request):
    data = {'data': 'data'}
    return render(request, 'posts/all_post.html', data)
