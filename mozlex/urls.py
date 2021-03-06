from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .examples import urls

from funfactory.monkeypatches import patch
patch()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'', include(urls)),

    # Generate a robots.txt
    (r'^robots\.txt$',
        lambda r: HttpResponse(
            "User-agent: *\n%s: /" % 'Allow' if settings.ENGAGE_ROBOTS else 'Disallow' ,
            mimetype="text/plain"
        )
    ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    # Mozilla Lexicon Entry
    url('', include('mozlex.lexicon.urls')),
)

## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    #urlpatterns += staticfiles_urlpatterns()
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
            url(r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
    )
