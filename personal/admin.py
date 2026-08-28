from django.contrib import admin
from .models import Empleado

# Registramos el modelo para que sea visible e interactivo en el panel /admin/
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'cargo', 'salario_mensual', 'esta_activo') # Columnas visibles en la tabla
    list_filter = ('esta_activo', 'cargo') # Filtros laterales derechos
    search_fields = ('nombre_completo', 'cargo') # Barra de búsqueda superior
