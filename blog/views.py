
from django.shortcuts import render, get_object_or_404
from .models import Tag, Article
from .models import Contact
from django.http import HttpResponse
from django.db.models import Q

def home(request):

    # feature articles on the home page
    featured = Article.articlemanager.filter(featured=True)[0:6]

    context = {
        'articles': featured
    }

    return render(request, 'index.html', context)


def articles(request):

    # get query from request
    query = request.GET.get('query')
    # print(query)
    # Set query to '' if None
    if query == None:
        query = ''

    # articles = Article.articlemanager.all()
    # search for query in headline, sub headline, body
    articles = Article.articlemanager.filter(
        Q(headline__icontains=query) |
        Q(sub_headline__icontains=query) |
        Q(body__icontains=query)
    )

    Tags = Tag.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'articles.html', context)


def article(request, article):

    article = get_object_or_404(Article, slug=article, status='published')

    context = {
        'article': article
    }

    return render(request, 'article.html', context)

def about(request):
     return render(request, 'about.html')    

def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobileno=request.POST.get('mobileno')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.mobileno=mobileno
        contact.message=message
        contact.save()
        return HttpResponse("<h1>THANKS FOR CONTACT US</h1>")
    return render(request, 'contact.html')


