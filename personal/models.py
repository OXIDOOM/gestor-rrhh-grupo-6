from django.db import models

# Definimos la tabla de empleados en la base de datos
class Empleado(models.Model):
    nombre_completo = models.CharField(max_length=150) # Campo de texto para el nombre
    cargo = models.CharField(max_length=100) # Campo de texto para el puesto
    salario_mensual = models.DecimalField(max_digits=10, decimal_places=2) # Campo numérico exacto para dinero
    esta_activo = models.BooleanField(default=True) # Interruptor de estado activo/inactivo

    class Meta:
        ordering = ['-salario_mensual'] # Ordena los registros automáticamente de mayor a menor salario

    def __str__(self):
        return self.nombre_completo # Muestra el nombre real en el panel de administración
