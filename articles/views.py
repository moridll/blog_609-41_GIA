from django.shortcuts import render

from .models import Article


def article_list(request):
    # return HttpResponse('<h1>Home</h1>')
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_item(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_item.html', {'article': article})
    # data = {
    #     "id": article_id
    # }
    # # return HttpResponse('<h1>Home</h1>')
    # return render(request, 'articles/article_item.html', data)