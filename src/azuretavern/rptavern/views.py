"""rptavern views."""

from django.views.generic import CreateView, ListView
from braces.views import LoginRequiredMixin
from .models import Character

class MyCharacterListView(LoginRequiredMixin, ListView):
    context_object_name = 'characters'

    def get_queryset(self):
        return Character.objects.filter(
            player=self.request.user,
        ).order_by('full_name')

    def get_context_data(self, **kwargs):
        context = super(MyCharacterListView, self).get_context_data(**kwargs)
        context['player'] = self.request.user
        return context

class CharacterCreateView(LoginRequiredMixin, CreateView):
    model = Character
    # TODO: Create a form class and use it to choose important fields

    def get_initial(self):
        return {
            'player': self.request.user,
        }
