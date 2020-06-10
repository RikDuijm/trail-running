from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Article


def get_articlesView(request):
    """
    View that will render the 'inspiration.html' template
    """
    return render(request, "inspiration.html")


def routes_destinationsView(request):
    """
    View that will return a list of Articles, filter them by catergory 'destinations' 
    and render them  to the Routes & Destinations template. 
    """
    articles = Article.objects.filter(category='destinations')
    return render(request, "routes_destinations.html", {'articles': articles})


def article_detailView(request, pk):
    """
    View that returns a single Article object based on the article ID (pk) and
    renders it to the 'article.html' template.
    Or return a 404 error if the article is not found
    """
    article = get_object_or_404(Article, pk=pk)
    article.views += 1
    article.save()
    return render(request, "article.html", {'article': article})
