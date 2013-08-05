#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail
from showtimeDuranjo.apps.homepage.forms import *
from showtimeDuranjo.apps.homepage.models import Galeria


def index(request, template='homepage/index.html', page_template='homepage/index_galeria.html'):
	success = False
	imagenes = Galeria.objects.all()
	if not imagenes:
		page_template='homepage/index_galeria_nohay.html'
		imagenes = None
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s mail: %s Tipo de servicio: %s Plan: %s' % (cd['nombre'], cd['email'], cd['tipoServicio'], cd['planes'])
			content = u'Email contacto: %s \nAsunto: %s \nTelefono: %s \nDescripcion: %s' % (cd['email'], asunto, cd['telefono'], cd['texto'])
			send_mail(asunto, content, cd['email'], ['info@duranjo.com'])
	else:
		form = contactForm()
	if request.is_ajax():
		template = page_template
	ctx = {'form': form, 'success': success, 'imagenes': imagenes, 'page_template': page_template}
	return render_to_response(template, ctx, context_instance=RequestContext(request))
