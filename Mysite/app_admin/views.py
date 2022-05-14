from django.views.generic import TemplateView, FormView
from django.shortcuts import render

from django.http import HttpResponse

from .forms import FeedbackForm


class IndexView(TemplateView):
    template_name = 'index.html'


class CollectionView(TemplateView):
    template_name = 'collection.html'


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = FeedbackForm


class RacingBootsView(TemplateView):
    template_name = 'racingboots.html'


class ShoesView(TemplateView):
    template_name = 'shoes.html'


def view_contact(request):
    return HttpResponse('<h1>Log is good </h1>')

def get_name(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        return render(request, 'contact.html', {'form': form})

