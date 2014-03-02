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
