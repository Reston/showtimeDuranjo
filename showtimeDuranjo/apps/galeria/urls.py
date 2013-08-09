from django.conf.urls import patterns, url

urlpatterns = patterns(
	'showtimeDuranjo.apps.galeria.views',
	url(r'^video/(?P<titulo>[-\w]+)/$', 'video', name="galeriavideo"),
	url(r'^album/(?P<titulo>[-\w]+)/$', 'album', name="galeriaalbum"),
	url(r'^galeria/$', 'galeria', name="galeriagaleria"),
)
