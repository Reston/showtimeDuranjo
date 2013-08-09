#!/usr/local/bin/python
# -*- encoding: utf-8 -*-
from django import forms


class VideoForm(forms.ModelForm):
	titulo = forms.RegexField(regex=r'^[\w ]+$', error_messages={'invalid': ("Caracteres invalidos.")})


class AlbumForm(forms.ModelForm):
	titulo = forms.RegexField(regex=r'^[\w ]+$', error_messages={'invalid': ("Caracteres invalidos.")})
