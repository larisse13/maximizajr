from django.contrib import admin
from .models import Quem_Somos
from .models import Portifolio
from .models import Servicos
from .models import Clientes

admin.site.register(Quem_Somos)
admin.site.register(Portifolio)
admin.site.register(Servicos)
admin.site.register(Clientes)

