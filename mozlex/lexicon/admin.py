from django.contrib import admin
from lexicon.models import Language, Entry, Translation

admin.site.register(Language)
admin.site.register(Entry)
admin.site.register(Translation)
