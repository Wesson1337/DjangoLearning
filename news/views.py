from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from news.models import News
from news.forms import NewsForm
from django.http import HttpResponseRedirect


class NewsList(ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'news_list.html'
    queryset = News.objects.all().order_by('date_added')


class NewsCreate(View):
    def get(self, request):
        news_form = NewsForm()
        return render(request, 'news_create.html', {'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'news_create.html', {'news_form': news_form})