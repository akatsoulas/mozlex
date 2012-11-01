# Create your views here.
from string import letters
from django.shortcuts import render_to_response
from models import Entry

def view_entry_list(request):
   ordered_entries = []
   for letter in letters[26:]:
       entries = Entry.live_entries.filter(lemma__istartswith=letter)
       if entries.count():
            ordered_entries.append({letter: entries})
   return render_to_response('lexicon_entry_list.html',
           {'entries_list': ordered_entries})
