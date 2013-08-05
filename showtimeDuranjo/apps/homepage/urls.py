from django.conf.urls import patterns, url

urlpatterns = patterns(
	'showtimeDuranjo.apps.homepage.views',
	url(r'^$', 'index', name="homepageindex"),
	url(r'^radio/$', 'radio', name="homepageradio"),
	url(r'^contacto/$', 'contacto', name="homepagecontacto"),
)

