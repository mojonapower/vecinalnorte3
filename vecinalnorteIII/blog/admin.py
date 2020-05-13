from django.contrib import admin
# Register your models here.

from .models import Material_mediomenor
from .models import Material_mediomayor
from .models import Material_medios
from .models import Material_salacuna
from .models import Material_cuentos

admin.site.register(Material_mediomenor)

admin.site.register(Material_mediomayor)

admin.site.register(Material_medios)

admin.site.register(Material_salacuna)

admin.site.register(Material_cuentos)
