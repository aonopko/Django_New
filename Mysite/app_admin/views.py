from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import FeedbackForm


class IndexView(TemplateView):
    template_name = 'index.html'


class CollectionView(TemplateView):
    template_name = 'collection.html'


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())


class RacingBootsView(TemplateView):
    template_name = 'racingboots.html'


class ShoesView(TemplateView):
    template_name = 'shoes.html'


def get_name(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        return render(request, 'index.html', {'form': form})
