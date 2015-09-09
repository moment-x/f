from django.conf.urls import url

from square.api import entry



urlpatterns = [
    url(r'^download/$', entry.download),
    url(r'^upload/$', entry.upload),
    url(r'^send/$', entry.send),
    url(r'^receive/$', entry.receive),
    url(r'^delivery/$', entry.in_delivery),
    url(r'^qsign/$', entry.qsign),

    url(r'^evernote_auth/$', entry.evernote_auth),
    url(r'^evernote_auth_callback/$', entry.evernote_auth_callback),

]
