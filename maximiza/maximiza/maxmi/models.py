from django.db import models

class Quem_SomosManager(models.Manager):

	def search(self, query):
		return self.get_queryset().filter(
			models.Q(title__icontains=query)| models.Q(description__icontains=query) 
		)

class PortifolioManager(models.Manager):

	def search(self, query):
		return self.get_queryset().filter(
			models.Q(title__icontains=query) 
		)

class ServicosManager(models.Manager):

	def search(self, query):
		return self.get_queryset().filter(
			models.Q(title__icontains=query) | models.Q(description__icontains=query) 
		)

class ClientesManager(models.Manager):

	def search(self, query):
		return self.get_queryset().filter(
			models.Q(title__icontains=query) | models.Q(description__icontains=query) 
		)

class BannerManager(models.Manager):

	def search(self, query):
		return self.get_queryset().filter(
			models.Q(title__icontains=query) | models.Q(description__icontains=query) 
		)

class Quem_Somos(models.Model):
	title= models.CharField('Titulo', max_length = 100)
	slug = models.SlugField('Atalho')
	description = models.TextField('Descrição', blank=True)
	start_date = models.DateField( 'Data de inicio', null=True, blank=True)
	image = models.ImageField(upload_to='media/quem_somos',verbose_name='Imagem',
		null=True , blank=True
		)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
	objects = Quem_SomosManager()

	def __str__(self):
		return self.title
	class Meta:
		verbose_name = 'Descrição/Foto'
		verbose_name_plural = 'Quem Somos'
		ordering = ['title']

class Portifolio(models.Model):
	title = models.CharField('Titulo',max_length=100)
	slug = models.SlugField('Atalho')
	description = models.TextField('Descrição', blank=True)
	start_date = models.DateField( 'Data de inicio', null=True, blank=True)
	image = models.ImageField(upload_to='media/portifolio',verbose_name='Imagem',
		null=True , blank=True
		)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
	objects = PortifolioManager()

	def __str__(self):
		return self.title
	class Meta:
		verbose_name = 'Portifolio'
		verbose_name_plural = 'Portifolio'
		ordering = ['title']

class Servicos(models.Model):
	title = models.CharField('Titulo', max_length=100)
	slug = models.SlugField('Atalho')
	start_date = models.DateField( 'Data de inicio', null=True, blank=True)
	image = models.ImageField(upload_to='media/servicos',verbose_name="Imagem", null=True , blank=True)
	brevedescri = models.CharField('Breve Descrição',max_length=200)
	completdescri= models.TextField('Descrição Completa', blank=True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
	objects = ServicosManager()
	
	def __str__(self):
		return self.title
	class Meta:
		verbose_name = 'Serviço'
		verbose_name_plural = 'Serviços'
		ordering = ['title']

class Clientes(models.Model):
	title = models.CharField('Titulo', max_length=100)
	slug = models.SlugField('Atalho')
	start_date = models.DateField( 'Data de inicio', null=True, blank=True)
	image = models.ImageField(upload_to='media/clientes',verbose_name="Imagem",null=True , blank=True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)
	objects = ClientesManager()
	
	def __str__(self):
		return self.title
	class Meta:
		verbose_name = 'Cliente'
		verbose_name_plural = 'Clientes'
		ordering = ['title']

class Banner(models.Model):
	title = models.CharField('Titulo', max_length=100)
	slug = models.SlugField('Atalho')
	start_date = models.DateField( 'Data de inicio', null=True, blank=True)
	image = models.ImageField(upload_to='media/banner',verbose_name="Imagem",null=True , blank=True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)
	objects = BannerManager()
	
	def __str__(self):
		return self.title
	class Meta:
		verbose_name = 'Banner'
		verbose_name_plural = 'Banners'
		ordering = ['title']