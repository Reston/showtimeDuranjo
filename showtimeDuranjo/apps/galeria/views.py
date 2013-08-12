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


def album(request, titulo):
	titulo = titulo.replace('_', ' ')
	album = get_object_or_404(Album, titulo=titulo)
	imagenes = ImgAlbum.objects.filter(album=album)
	ctx = {'album': album, 'imagenes': imagenes}
	return render_to_response('galeria/album.html', ctx, context_instance=RequestContext(request))


def galeria(request, template='galeria/galeria.html', page_template='galeria/galeria_lista.html'):
	lista_galeria = sorted(chain(Album.objects.all(), Video.objects.all()), key=attrgetter('creado_en'), reverse=True)
	ctx = {'lista_galeria': lista_galeria , 'page_template': page_template}
	if request.is_ajax():
		template = page_template	
	return render_to_response(template, ctx, context_instance=RequestContext(request))
