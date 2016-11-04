from django.shortcuts import get_object_or_404, render
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('-created_date')[:5]
    return render(request, 'post_list.html', {'posts': posts})

def single_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'single_post.html', {'post': post})
