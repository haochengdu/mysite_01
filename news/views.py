from django.shortcuts import render
from .models import Article


def year_archive(request, year):
    article_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year}
    return render(request, 'news/year_archive.html', locals())



