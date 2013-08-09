# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse


class Video(models.Model):
	titulo = models.CharField(max_length=20, help_text='Hasta 20 caracteres y solamente alfanuméricos')
	enlace_video = models.CharField(max_length=45) 
	breve_descripcion = models.CharField(max_length=140, help_text='Hasta 140 caracteres')
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)
	es_video = models.BooleanField(default=True, editable=False)

	def __unicode__(self):
		return self.titulo

	def get_absolute_url(self):
		titulo = self.titulo.replace(' ', '_')
		return reverse('Video', kwargs={'titulo': titulo})


class Album(models.Model):
	titulo = models.CharField(max_length=25, help_text='Hasta 25 caracteres y solamente alfanuméricos')
	descripcion_corta = models.CharField(max_length=140, help_text='Hasta 140 caracteres')
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)
	es_video = models.BooleanField(default=False, editable=False)

	def __unicode__(self):
		return self.titulo

	def get_absolute_url(self):
		titulo = self.titulo.replace(' ', '_')
		return reverse('album', kwargs={'titulo': titulo})


class ImgAlbum(models.Model):
	album = models.ForeignKey(Album, related_name='imagenes')
	imagen = models.ImageField(upload_to='imgalbum')
