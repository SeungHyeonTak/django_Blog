from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog
from django.contrib.auth import get_user_model

def blog_list(request):
    #blogs = Blog.objects.all()
    blogs = Blog.objects.filter(published_date__isnull=False).order_by('-created_date')
    context = {
        'blogs':blogs
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog':blog
    }
    return render(request, 'blog/blog_detail.html', context)


def blog_add(request):
    if request.method == 'POST':
        User = get_user_model()
        author = User.objects.get(username='admin')
        title = request.POST['title']
        content = request.POST['content']
        post = Blog.objects.create(
            author=author,
            title=title,
            content=content,
        )
        post.publish()
        # 등록한 글의 기본키를 가져와서 post_pk 변수에 할당.
        post_pk = post.pk
        # 기본키를 전달한 post_detail 뷰를 redirect 함수에 전달.
        return redirect(blog_detail, pk=post_pk)
    elif request.method == 'GET':
        return render(request, 'blog/blog_add.html')


def blog_delete(request, pk):
    if request.method == "POST":
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return render(request, 'blog/blog_delete.html')
    elif request.method == "GET":
        return HttpResponse('잘못된 접근 입니다.')