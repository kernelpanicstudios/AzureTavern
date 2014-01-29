"""Site-wide views for the Azure Tavern."""

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'
