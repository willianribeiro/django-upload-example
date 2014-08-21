from django.db import models

class Document(models.Model):
	# ModelField para arquivos -> FileField
	doc_file = models.FileField(upload_to='documents/%Y/%m/%d')
