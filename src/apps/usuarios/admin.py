from django.contrib import admin


from .models import Usuarios
# Register your models here.

# me quede en el video en la parte o hora: 1:42:04 de Django apps + sttings + models

class UsuariosAdmin(admin.ModelAdmin): 
	list_display = ['id', 'nombre', 'apellido']


admin.site.register(Usuarios,UsuariosAdmin)