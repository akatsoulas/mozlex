from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('mozlex.lexicon.views',
        url(r'^lexicon/$', 'view_entry_list'),
        url(r'^lexicon/edit/(?P<lemma>\w+)/$', 'view_edit_entry'),
)
