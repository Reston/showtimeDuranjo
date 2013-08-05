from django.conf.urls import patterns, url

urlpatterns = patterns(
	'conbuenpieDuranjo.apps.homepage.views',
	url(r'^$', 'index', name="homepageindex"),
)

