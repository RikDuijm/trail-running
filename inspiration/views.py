from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Article


def get_articlesView(request):
    """
    Create a view that will return a list
    of Articles and render them to the 'inspiration.html' template
    """
    articles = Article.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date').all()
    return render(request, "inspiration.html", {'articles': articles})


def article_detailView(request, pk):
    """
    Create a view that returns a single
    Article object based on the article ID (pk) and
    render it to the 'article.html' template.
    Or return a 404 error if the article is
    not found
    """
    article = get_object_or_404(Article, pk=pk)
    article.views += 1
    article.save()
    return render(request, "article.html", {'article': article})
