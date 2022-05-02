from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class CollectionView(TemplateView):
    template_name = 'collection.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class RacingBootsView(TemplateView):
    template_name = 'racingboots.html'


class ShoesView(TemplateView):
    template_name = 'shoes.html'
