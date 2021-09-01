from django.shortcuts 				import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins 	import LoginRequiredMixin
from django.views.generic 			import ListView
from .models 						import Usuarios
from .forms 						import AmigoForm
# Create your views here.
"""
def listar_usuarios(request): 
	template_name = "usuarios/listarusuarios.html"
	lista_de_usuarios = Usuarios.objects.all()
	ctx = {
		'usuarios' : lista_de_usuarios
	}
	return render(request, template_name, ctx)
"""



def nuevo_amigo(request): 
	template_name = "usuarios/nuevo.html"
	ctx = {
		'form': AmigoForm()
	}
	return render(request, template_name, ctx)


class Listar(LoginRequiredMixin, ListView): 
	template_name = "usuarios/listarusuarios.html" # Seguir despues, tiene un error... video Vistas basadas en funciones
													# y en clases--- 10: 00
	model = Usuarios
	
	context_object_name = 'usuarios'

	def get_queryset(self): 
		if self.request.user.is_superuser: 
			return Usuarios.objects.all()
		

		return Usuarios.objects.filter(nombre="Belen")

	"""
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["color"] = "amarillo"
		return context
	"""