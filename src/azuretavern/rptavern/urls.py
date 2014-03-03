"""RPTavern URLs."""

from django.conf.urls import include, patterns, url
from .views import (MyCharacterListView, CharacterCreateView,
    CharacterEditView, CharacterDetailsView, GameCreateView)

urlpatterns = patterns('',
    url(r'characters/me$', MyCharacterListView.as_view(),
        name='my-characters',
    ),
    url(r'characters/new$', CharacterCreateView.as_view(),
        name='new-character',
    ),
    url(r'characters/(?P<pk>\d+)/details$', CharacterDetailsView.as_view(),
        name='character-details',
    ),
    url(r'characters/(?P<pk>\d+)/edit$', CharacterEditView.as_view(),
        name='update-character',
    ),
    url(r'games/new$', GameCreateView.as_view(),
        name='new-game',
    ),
)
