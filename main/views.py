import datetime as dt

import humanize
import pytz
from django.shortcuts import render, redirect

from .forms import NewsForm
from .models import News


# Create your views here.


def index(request):
    _t = humanize.i18n.activate("ru_RU")
    if request.GET.get('search'):
        listOfNews = News.objects.filter(Tags__name=request.GET.get('search'))

    else:
        listOfNews = News.objects.order_by('-id')
    context = []
    if not listOfNews.exists():
        return render(request, 'main/404.html')
    for news in listOfNews:
        now = dt.datetime.utcnow()
        now = now.replace(tzinfo=pytz.utc)
        delta = humanize.naturaltime(now - news.TimeCreate)
        context.append({'news': news, 'delta': delta})

    return render(request, 'main/index.html', {'context': context})


def NewsList(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = NewsForm()
    context = {
        "form": form
    }
    return render(request, "main/createNews.html", context)


def NewsPaper(request):
    if not News.objects.filter(id=request.GET.get('id')).exists():
        return render(request, 'main/404.html')
    else:
        paperNews = News.objects.filter(id=request.GET.get('id')).get()
    context = {
        "paperNews": paperNews
    }
    return render(request, "main/NewsPaper.html", context)
