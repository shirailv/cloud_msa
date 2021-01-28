from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from myapp.models import Post
# Create your views here.

def post_add(request):
    if request.method == 'POST':
        User = get_user_model()
        author = User.objects.get(username='junmo')
        title = request.POST['title']
        content = request.POST['content']
        post = Post.objects.create(
            author=author,
            title=title,
            content=content,
        )
        post.publish()
        post_pk = post.pk
        return redirect(post_detail, pk=post_pk)
    elif request.method == 'GET':
        return render(request, 'myapp/post_add.html')
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'myapp/index.html', context)

def post_detail(request, pk):  
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'myapp/post_detail.html', context)

def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
        return render(request, 'myapp/post_delete.html')

    elif request.method == 'GET':
        return HttpResponse('잘못된 접근 입니다.')
