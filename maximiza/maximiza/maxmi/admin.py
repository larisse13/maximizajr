from django.contrib import admin
from .models import Quem_Somos
from .models import Portifolio
from .models import Servicos
from .models import Banner
from .models import Clientes

class Quem_SomosAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug' ,'start_date', 'created_at', 'updated_at']
	search_fields = ['title', 'slug']
	prepopulated_fields = {'slug':('title',)}

admin.site.register(Quem_Somos, Quem_SomosAdmin)
admin.site.register(Portifolio, Quem_SomosAdmin)
admin.site.register(Servicos, Quem_SomosAdmin)
admin.site.register(Clientes, Quem_SomosAdmin)
admin.site.register(Banner, Quem_SomosAdmin)

