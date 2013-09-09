#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail
from showtimeDuranjo.apps.homepage.forms import *
from showtimeDuranjo.apps.homepage.models import Galeria
from zinnia.models import Entry
import nltk


def index(request):
	entradas= Entry.objects.order_by('-creation_date')
	entradas= entradas[:4]
	for ent in entradas:
		quitar_html= nltk.clean_html(ent.content) 
		ent.content =  quitar_html[:65]
	ctx = {'entradas':entradas}
	return render_to_response('homepage/index.html', ctx, context_instance=RequestContext(request))

def contacto(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s mail: %s' % (cd['nombre'], cd['email'])
			content = u'Email contacto: %s \nAsunto: %s \nTelefono: %s \nDescripcion: %s' % (cd['email'], asunto, cd['telefono'], cd['texto'])
			send_mail(asunto, content, 'contacto@showtimenews.com.ve', ['contacto@showtimenews.com.ve'])
	else:
		form = contactForm()
	ctx = {'form': form, 'success': success}
	return render_to_response('homepage/contacto.html', ctx, context_instance=RequestContext(request))


def radio(request , template='homepage/radio.html', page_template='homepage/radio_galeria.html'):
	imagenes = Galeria.objects.all()
	if not imagenes:
		page_template='homepage/radio_galeria_nohay.html'
		imagenes = None
	if request.is_ajax():
		template = page_template
	ctx = {'imagenes': imagenes, 'page_template': page_template}
	return render_to_response(template, ctx, context_instance=RequestContext(request))