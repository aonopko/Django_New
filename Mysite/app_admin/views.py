from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect

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


def get_name(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        return redirect(request, 'index.html', {'form': form})

