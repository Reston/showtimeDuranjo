#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from showtimeDuranjo.apps.galeria.models import Video, Album, ImgAlbum
from django.shortcuts import get_object_or_404
from itertools import chain
from operator import attrgetter

def video(request, titulo):
	titulo = titulo.replace('_', ' ')
	video = get_object_or_404(Video, titulo=titulo)
	ctx = {'video': video}
	return render_to_response('galeria/video.html', ctx, context_instance=RequestContext(request))


def album(request, template='galeria/album.html', page_template='galeria/album_imagenes.html', titulo=None):
	palabra_busqueda = request.POST.get('busqueda', '')
	mensaje = ''
	titulo = titulo.replace('_', ' ')
	album = Album.objects.get(titulo=titulo)
	imagenes = ImgAlbum.objects.filter(album__in=album)
	if request.is_ajax():
		template = page_template
	if (palabra_busqueda):
		albumes = Album.objects.filter(titulo__icontains=palabra_busqueda)
		if not (albumes):
			mensaje = "No se han encontrado resuldos para "+palabra_busqueda
	ctx = {
		'page_template': page_template,
		'imagenes': imagenes,
		'mensaje': mensaje
	}
	return render_to_response(template, ctx, context_instance=RequestContext(request))


def galeria(request, template='galeria/galeria.html', page_template='galeria/galeria_lista.html'):
	lista_galeria = sorted(chain(Album.objects.all(), Video.objects.all()), key=attrgetter('creado_en'))
	for li in lista_galeria:
		print li
		print "PRUEBA: "+li.titulo
		if li.es_video:
			print " ¿Es video?  SI"
		else:
			print " ¿Es video? NO"
	ctx = {'lista_galeria': lista_galeria , 'page_template': page_template}
	if request.is_ajax():
		template = page_template	
	return render_to_response(template, ctx, context_instance=RequestContext(request))
