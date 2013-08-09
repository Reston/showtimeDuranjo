from django.contrib import admin
#from django.contrib.contenttypes import generic
from showtimeDuranjo.apps.galeria.models import Video, Album, ImgAlbum
from showtimeDuranjo.apps.galeria.forms import VideoForm, AlbumForm


class VideoAdmin(admin.ModelAdmin):
	form = VideoForm
	list_display = ('titulo', 'breve_descripcion', 'creado_en', 'modificado_en')
	list_display_links = ('titulo',)
	search_fields = ['titulo', 'breve_descripcion']


class ImgAlbumInline(admin.TabularInline):
	model = ImgAlbum


class AlbumAdmin(admin.ModelAdmin):
	form = AlbumForm
	list_display = ('titulo', 'descripcion_corta', 'creado_en', 'modificado_en')
	list_display_links = ('titulo', 'descripcion_corta',)
	#list_filter = ('disponible', 'destacado', 'categoria')
	search_fields = ['titulo']
	inlines = [
		ImgAlbumInline,
	]


admin.site.register(Video, VideoAdmin)
admin.site.register(Album, AlbumAdmin)
