from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
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
        ).order_by('-published_date')
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
 
 