from django.conf.urls import patterns, url

urlpatterns = patterns(
	'showtimeDuranjo.apps.homepage.views',
	url(r'^$', 'index', name="homepageindex"),
)

