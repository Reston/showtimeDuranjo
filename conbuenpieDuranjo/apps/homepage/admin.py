from django.contrib import admin
#from django.contrib.contenttypes import generic
from conbuenpieDuranjo.apps.homepage.models import Galeria


class GaleriaAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'creado_en', 'modificado_en')
	list_display_links = ('titulo',)
	search_fields = ['titulo']

admin.site.register(Galeria, GaleriaAdmin)