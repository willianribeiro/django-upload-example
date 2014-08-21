# coding=UTF-8

from django import forms

class DocumentForm(forms.Form):
	doc_file = forms.FileField(
		label='Selecione um arquivo',
		help_text='Tamanho máximo: x MB'
	)