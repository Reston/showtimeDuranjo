# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse

class Galeria(models.Model):
	imagen = models.ImageField(upload_to='galeria')
	titulo = models.CharField(max_length=30)
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.titulo

	def get_absolute_url(self):
		titulo = self.titulo.replace(' ', '_')
		return reverse('indexindex', kwargs={'titulo': titulo})

	class Meta:
		verbose_name = 'Galeria de la radio'
		verbose_name_plural = 'Galeria de la radio'
