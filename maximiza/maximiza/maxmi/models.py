from django.db import models

class Quem_Somos(models.Model):
	title= models.CharField('Titulo', max_length = 100)
	description = models.TextField('Descrição', blank=True)
	image = models.ImageField(upload_to='midia/quem_somos',verbose_name='Imagem',
		null=True , blank=True
		)
	def __str__(self):
		return self.title
	class Meta:
		verbose_name = 'Descrição/Foto'
		verbose_name_plural = 'Quem Somos'
		ordering = ['title']

class Portifolio(models.Model):
	title = models.CharField('Titulo',max_length=100)
	image = models.ImageField(upload_to='midia/portifolio',verbose_name='Imagem',
		null=True , blank=True
		)
	def __str__(self):
		return self.title
	class Meta:
		verbose_name = 'Portifolio'
		verbose_name_plural = 'Portifolio'
		ordering = ['title']

class Servicos(models.Model):
	title = models.CharField('Titulo', max_length=100)
	image = models.ImageField(upload_to='midia/servicos',verbose_name="Imagem")
	brevedescri = models.CharField('Breve Descrição',max_length=200)
	completdescri= models.TextField('Descrição Completa', blank=True)

	def __str__(self):
		return self.title
	class Meta:
		verbose_name = 'Serviço'
		verbose_name_plural = 'Serviços'
		ordering = ['title']

class Clientes(models.Model):
	title = models.CharField('Titulo', max_length=100)
	image = models.ImageField(upload_to='midia/clientes',verbose_name="Imagem")

	def __str__(self):
		return self.title
	class Meta:
		verbose_name = 'Cliente'
		verbose_name_plural = 'Clientes'
		ordering = ['title']