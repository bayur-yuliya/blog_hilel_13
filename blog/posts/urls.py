from django.urls import path

from posts import views

urlpatterns = [
    path('', views.posts, name='all_posts'),
    path('post/<int:post_id>', views.get_post, name='post')
]