"""RPTavern URLs."""

from django.conf.urls import include, patterns, url
from .views import MyCharacterListView, CharacterCreateView

urlpatterns = patterns('',
    url('characters/me', MyCharacterListView.as_view(),
        name='my-characters'
    ),
    url('characters/new', CharacterCreateView.as_view(),
        name='new-character'
    ),
)
