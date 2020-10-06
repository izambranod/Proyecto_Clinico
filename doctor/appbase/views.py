from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Paciente, Doctor, Horario
from .forms import PacienteForm, DoctorForm, HorarioForm

class InicioView(TemplateView):
    template_name = "index.html"


#    Crea un nuevo registro de los pacientes
class CrearPacienteView(CreateView):
    model = Paciente
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/paciente/registrar_paciente.html"
    form_class = PacienteForm
    success_url = reverse_lazy('base:paciente')
    context_object_name = "pacientes"



class PacienteView(ListView):
    model = Paciente
    template_name = "base/paciente/paciente.html"
    context_object_name = "pacientes"
    #queryset = Paciente.objects.filter(estado=False)
    paginate_by = 3

    def get_queryset(self):
        nombre = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        return self.model.objects.filter(nombre__icontains=nombre, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        context['titulo'] = "Consulta de pacientes"
        return context

class EditarPacienteView(UpdateView):
    model = Paciente
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/paciente/registrar_paciente.html"
    form_class = PacienteForm
    success_url = reverse_lazy('base:paciente')
    context_object_name = "pacientes"


class EliminarPacienteView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        paciente = Paciente.objects.get(id=pk)
        paciente.delete()
        # object.estado = False
        # object.save()
        return redirect('base:paciente')

#    Crea un nuevo registro de los pacientes
class CrearDoctorView(CreateView):
    model = Doctor
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/doctor/registrar_doctor.html"
    form_class = DoctorForm
    success_url = reverse_lazy('base:paciente')
    context_object_name = "doctores"


class CrearHorarioView(CreateView):
    model = Horario
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/horario/registrar_horario.html"
    form_class = HorarioForm
    success_url = reverse_lazy('base:paciente')
    context_object_name = "horarios"