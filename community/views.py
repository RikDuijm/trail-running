from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from accounts.models import UserProfile
from .forms import BlogPostForm
from django.http import HttpResponseForbidden
from django.contrib import messages


def get_posts(request):
    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to the 'blogposts.html' template
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date').all()
    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})


def new_post(request, pk=None):
    """
    Create a view that allows user to add new post
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('get_posts')
        else:
            form = BlogPostForm()
    else:
        return redirect('login')        
    return render(request, 'blogpostform.html', {'form': form})
 

def edit_post(request, pk=None):
    """
    Create a view that allows user to edit
    his own post  and a superuser to edit every post.
    """
    post = get_object_or_404(Post, pk=pk)
    if (request.user == post.author or
            request.user.is_superuser):
        if request.method == "POST":
            form = BlogPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save()
                return redirect(post_detail, post.pk)
        else:
            form = BlogPostForm(instance=post)
    else:
        return HttpResponseForbidden()

    return render(request, 'blogpostform.html', {'form': form})


def delete_post(request, pk=None):
    """
    Create a view that allows user to delete
    his own post  and a superuser to delete every post.
    """
    post = get_object_or_404(Post, pk=pk)
    author = post.author
    if request.user == author or request.user.is_superuser:
        if request.method == "POST":
            post.delete()
            messages.success(request, 'Your post has been successfully deleted.')
            return redirect('get_posts')
    return render(request, "postdelete.html", {'post': post})


def author_profile(request, pk=None):
    """The profile of the author of the blogpost"""
    post = get_object_or_404(Post, pk=pk)
    author = post.author
    return render(request, 'profile.html', {"profile": author})