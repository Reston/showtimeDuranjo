#-*- encoding: utf-8 -*-
from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from showtimeDuranjo.apps.galeria.models import Video, Album

class StaticViewSitemap(sitemaps.Sitemap):
	priority = 0.5
	changefreq = 'daily'

	def items(self):
		return [
				'homepageindex',
				'homepageradio',
				'homepagecontacto',
				'galeriagaleria',
				# colocar los nombre de las url en este lugar. ejemplo: 'homepageworks'
				]

	def location(self, item):
		return reverse(item)

class VideoSitemap(sitemaps.Sitemap):
	changefreq = 'monthly'
	priority = 0.6

	def items(self):
		return Video.objects.all()

	def lastmod(self, obj):
		return obj.modificado_en


class AlbumSitemap(sitemaps.Sitemap):
	changefreq = 'monthly'
	priority = 0.6

	def items(self):
		return Album.objects.all()

	def lastmod(self, obj):
		return obj.modificado_en