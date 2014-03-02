"""RPTavern URLs."""

from django.conf.urls import include, patterns, url
from .views import (MyCharacterListView, CharacterCreateView,
    CharacterDetailsView)

urlpatterns = patterns('',
    url(r'characters/me$', MyCharacterListView.as_view(),
        name='my-characters',
    ),
    url(r'characters/new$', CharacterCreateView.as_view(),
        name='new-character',
    ),
    url(r'characters/details/(?P<pk>\d+)$', CharacterDetailsView.as_view(),
        name='character-details',
    ),
)
