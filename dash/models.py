from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import (CreationDateTimeField,
                                         ModificationDateTimeField,
                                         AutoSlugField)

# Create your models here.


class Palestra(models.Model):
    talk_name = models.CharField(
        _('Nome da palestra'), max_length=45, unique=True)
    talk_description = models.CharField(
        _('Descrição da palestra'), max_length=90)
    speaker_name = models.CharField(_('Nome do palestrante'), max_length=45)
    speaker_description = models.CharField(
        _('Sobre o palestrante'), max_length=45, null=True)
    local = models.CharField(_('Prédio/Bloco da palestra'),
                             help_text=_('Exemplo: Bloco X'), max_length=30)
    room = models.CharField(_('Sala da palestra'), max_length=30)
    date = models.DateField(_('Data'))
    hour_init = models.TimeField(_('Início'))
    hour_end = models.TimeField(_('Término'))
    number_vacancies = models.SmallIntegerField(_('Vagas'))
    created = CreationDateTimeField()
    modification = ModificationDateTimeField()
    slug = AutoSlugField(populate_from=['talk_name', 'speaker_name'])

    def __str__(self):
        return '{} - {}'.format(self.talk_name, self.speaker_name)
