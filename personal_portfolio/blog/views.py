from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required


def hello(request):
    text = """<h1>welcome to my app !</h1>"""
    return HttpResponse(text)


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = Comment(
                    author=form.cleaned_data["author"],
                    body=form.cleaned_data["body"],
                    post=post
                )
                comment.save()

        comments = Comment.objects.filter(post=post)
        context = {
            "post": post,
            "comments": comments,
            "form": form,
        }

    except Post.DoesNotExist:
        return HttpResponseNotFound("Blog post not found.")

    return render(request, "blog_detail.html", context)
