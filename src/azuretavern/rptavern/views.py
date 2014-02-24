"""rptavern views."""

from django.views.generic import CreateView, ListView
from braces.views import LoginRequiredMixin
from .models import Character

class MyCharacterListView(LoginRequiredMixin, ListView):
    context_object_name = 'characters'

    def get_queryset(self):
        return Character.objects.filter(
            player=self.request.user
        ).order_by('full_name')

    def get_context_data(self, **kwargs):
        context = super(MyCharacterListView, self).get_context_data(**kwargs)
        context['is_me'] = True
        return context

class CharacterCreateView(LoginRequiredMixin, CreateView):
    model = Character

    def get_initial(self):
        return {
            'player': self.request.user,
        }
