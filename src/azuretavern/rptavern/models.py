"""Models needed for the RPTavern."""

from django.core import urlresolvers
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Character(models.Model):
    MALE = 'm'
    FEMALE = 'f'
    GENDER_CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female')),
    )

    player = models.ForeignKey(User)
    full_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=60)
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES, blank=True)
    description = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'modified_date'
        unique_together = ('player', 'full_name')
        verbose_name = _('character')
        verbose_name_plural = _('characters')

    def get_absolute_url(self):
        return urlresolvers.reverse(
            'character-details',
            kwargs={'pk': self.id},
        )

    def __unicode__(self):
        return self.full_name

class Game(models.Model):
    gm = models.ForeignKey(User)
    title = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    players = models.ManyToManyField(
        User,
        through='GamePlayer',
        related_name='players',
    )

class GamePlayer(models.Model):
    game = models.ForeignKey(Game)
    player = models.ForeignKey(User)

class CharacterNote(models.Model):
    PRIVATE = 'pr'
    LIMITED = 'li'
    PUBLIC = 'pu'
    PERMISSION_CHOICES = (
        (PRIVATE, _('Private')),
        (LIMITED, _('Limited')),
        (PUBLIC, _('Public')),
    )

    character = models.ForeignKey(Character)
    title = models.CharField(max_length=100, blank=True)
    text = models.CharField(max_length=4000)
    permissions = models.CharField(max_length=3, choices=PERMISSION_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        order_with_respect_to = 'character'
