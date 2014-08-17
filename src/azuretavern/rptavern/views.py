"""rptavern views."""

from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from braces.views import LoginRequiredMixin, UserFormKwargsMixin
from .forms import CharacterForm, GameForm
from .models import Character, Game

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
    form_class = CharacterForm

    def get_initial(self):
        return {
            'player': self.request.user,
        }

class CharacterEditView(LoginRequiredMixin, UserFormKwargsMixin, UpdateView):
    model = Character
    form_class = CharacterForm

    def get_initial(self):
        return {
            'player': self.request.user,
        }

class CharacterDetailsView(LoginRequiredMixin, DetailView):
    model = Character

class GameCreateView(LoginRequiredMixin, UserFormKwargsMixin, CreateView):
    model = Game
    form_class = GameForm

    def get_initial(self):
        return {
            'gm': self.request.user,
        }

class AbstractGameGMListView(LoginRequiredMixin, ListView):
    context_object_name = 'games'

    def get_gm(self):
        raise ImproperlyConfigured('get_gm() must be configured')

    def get_queryset(self):
        return Game.objects.filter(
            gm=self.get_gm(),
        ).order_by('title')

    def get_context_data(self, **kwargs):
        context = super(AbstractGameGMListView, self).get_context_data(**kwargs)
        context['gm'] = self.get_gm()
        return context

class MyGameGMListView(AbstractGameGMListView):
    def get_gm(self):
        return self.request.user
