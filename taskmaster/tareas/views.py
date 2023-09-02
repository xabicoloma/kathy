from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from .models import Tarea
from .forms.tareas.forms import TareaForm
from django.contrib import messages
from django.views.generic import  UpdateView

# Create your views here.
def index(request):
    return render(request,"tareas/index.html")

"""def home(request):
    return render(request,"tareas/home.html")"""



def crear_posteo(request):

    form = TareaForm()
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data["titulo"]
            descripcion = form.cleaned_data["descripcion"]
            vencimiento = form.cleaned_data["vencimiento"]
            estados = form.cleaned_data["estados"]
            identificador  = form.cleaned_data["identificador"]
            etiqueta_tarea = form.cleaned_data["etiqueta_tarea"]
            post = Tarea(
                titulo=titulo,
                descripcion=descripcion,
                vencimiento=vencimiento,
                estados=estados,
                identificador = identificador,
                etiqueta_tarea = etiqueta_tarea
            )
            post.save()
            return redirect('home')
        else:
            return render(request, 'tareas/layouts/partials/crearTarea.html', {"form":form})

    return render(request, 'tareas/layouts/partials/crearTarea.html', {"form":form})


def eliminar_posteo(request, id):

    post = Tarea.objects.get(pk=id)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Se elimino exitosamente!')
        return redirect('home')


def listarTarea(request):
    tarea = Tarea.objects.all()
    return render(request, 'tareas/home.html' ,{"context": tarea})

class PostUpdateView(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/layouts/partials/editarTarea.html'
    success_url = reverse_lazy('home')