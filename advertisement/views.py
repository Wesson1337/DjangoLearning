from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from advertisement.models import Advertisement


def advertisement_list(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisement_list.html', {
        'advertisements': advertisements
    })


class About(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Иду гулять с собакой'
        context['title'] = 'Прогулка с собаками'
        context['description'] = 'Гуляю с собакой недорого.'
        return context
