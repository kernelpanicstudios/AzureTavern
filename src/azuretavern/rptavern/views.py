"""rptavern views."""

from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from braces.views import LoginRequiredMixin, UserFormKwargsMixin
from .forms import CharacterCreateForm
from .models import Character

class AbstractCharacterListView(LoginRequiredMixin, ListView):
    context_object_name = 'characters'

    def get_player(self):
        raise ImproperlyConfigured('get_player() must be configured')

    def get_queryset(self):
        return Character.objects.filter(
            player=self.get_player(),
        ).order_by('full_name')

    def get_context_data(self, **kwargs):
        context = super(AbstractCharacterListView, self).get_context_data(**kwargs)
        context['player'] = self.get_player()
        return context

class MyCharacterListView(AbstractCharacterListView):
    def get_player(self):
        return self.request.user

class CharacterListView(AbstractCharacterListView):
    player_id = None

    def get_player(self):
        if self.player_id is None:
            raise ImproperlyConfigured('player_id must be provided')
        return get_object_or_404(User, pk=self.player_id)

class CharacterCreateView(LoginRequiredMixin, UserFormKwargsMixin, CreateView):
    model = Character
    form_class = CharacterCreateForm

    def get_initial(self):
        return {
            'player': self.request.user,
        }

class CharacterDetailsView(LoginRequiredMixin, DetailView):
    model = Character
