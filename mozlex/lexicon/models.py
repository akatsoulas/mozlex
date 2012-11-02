import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=50,
            help_text='Maximum 50 Characters')
    language_code = models.CharField(max_length=5,
            help_text='Maximum 5 Characters')
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['language_code']

    def __unicode__(self):
        return self.name


#Overide Manager
class LiveEntryManager(models.Manager):
    def get_query_set(self):
        return super(LiveEntryManager, self).get_query_set().filter(
                status=self.model.LIVE_STATUS)


class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    #Page Status Enumeration
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )
    #Managers
    live_entries = LiveEntryManager()
    objects = models.Manager()
    #Core Fields
    lemma = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=False)
    pud_date = models.DateTimeField(editable=False)
    updated_date = models.DateField(editable=False)
    author = models.ForeignKey(User)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)

    class Meta:
        verbose_name_plural = 'Entries'
        ordering = ['lemma']

    def __unicode__(self):
        return self.lemma

    @models.permalink
    def get_absolute_url(self):
        return('lexicon_edit_entry', (), {'lemma': self.lemma})

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.pud_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        super(Entry, self).save(force_insert, force_update)


class Translation(models.Model):
    translation = models.TextField(blank=False)
    language = models.ForeignKey(Language)
    entry = models.ForeignKey(Entry)

    def __unicode__(self):
        return self.translation

    def live_entry_set(self):
        return self.entry_set.filter(status=Entry.LIVE_STATUS)
