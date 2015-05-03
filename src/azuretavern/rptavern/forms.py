"""rptavern forms."""

from django import forms
from django.forms.models import inlineformset_factory
from django.utils.translation import ugettext_lazy as _
from braces.forms import UserKwargModelFormMixin
from rptavern.models import Character, Game, CharacterNote

class CharacterForm(UserKwargModelFormMixin, forms.ModelForm):
    class Meta:
        model = Character
        fields = ['player', 'short_name', 'full_name', 'gender', 'description']
        widgets = {
            'player': forms.HiddenInput,
        }

    def clean_player(self):
        if self.cleaned_data['player'] != self.user:
            raise forms.ValidationError(
                _('You cannot create characters for other users'),
                code='invalid_player',
            )
        return self.cleaned_data['player']

class GameForm(UserKwargModelFormMixin, forms.ModelForm):
    class Meta:
        model = Game
        fields = ['gm', 'title', 'subtitle', 'description']
        widgets = {
            'gm': forms.HiddenInput,
        }

    def clean_gm(self):
        if self.cleaned_data['gm'] != self.user:
            raise forms.ValidationError(
                _('You cannot create games for other users to GM'),
                code='invalid_gm',
            )
        return self.cleaned_data['gm']

class CharacterNoteForm(UserKwargModelFormMixin, forms.ModelForm):
    class Meta:
        model = CharacterNote
        fields = ['character', 'title', 'text', 'permissions']
        widgets = {
            'character': forms.HiddenInput,
        }

    def clean_character(self):
        if self.cleaned_data['character'].player != self.user:
            raise forms.ValidationError(
                _('You cannot create or edit notes for characters that do not'
                    'belong to you'),
                code='character_permission_denied',
            )
        return self.cleaned_data['character']

CharacterNotesFormSet = inlineformset_factory(
    Character,
    CharacterNote,
    form=CharacterNoteForm,
)
