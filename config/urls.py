from django.contrib import admin
from django.urls import path, include

# Redirigimos el tráfico web hacia las reglas configuradas en nuestra aplicación 'personal'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('personal.urls')), 
]
