from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Paciente, Doctor, Horario, Agenda, SignoVital
from .forms import PacienteForm, DoctorForm, HorarioForm, AgendaForm, SignoForm

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
    # paginate_by = 3

    # def get_queryset(self):
    #     nombre = self.request.GET.get(
    #         'nombre') if self.request.GET.get('nombre') else ''
    #     return self.model.objects.filter(nombre__icontains=nombre, estado=True)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['nombre'] = self.request.GET.get(
    #         'nombre') if self.request.GET.get('nombre') else ''
    #     context['titulo'] = "Consulta de pacientes"
    #     return context

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
    success_url = reverse_lazy('base:doctor')
    context_object_name = "doctores"

class EliminarDoctorView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        doctor = Doctor.objects.get(id=pk)
        doctor.delete()
        # object.estado = False
        # object.save()
        return redirect('base:doctor')

class CrearHorarioView(CreateView):
    model = Horario
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/horario/registrar_horario.html"
    form_class = HorarioForm
    success_url = reverse_lazy('base:horario')
    context_object_name = "horarios"

class HorarioView(ListView):
    model = Horario
    template_name = "base/horario/horario.html"
    context_object_name = "horarios"

class CrearAgendaView(CreateView):
    model = Agenda
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/agenda/registrar_agenda.html"
    form_class = AgendaForm
    success_url = reverse_lazy('base:agenda')
    context_object_name = "agendas"

class EliminarAgendaView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        agenda = Agenda.objects.get(id=pk)
        agenda.delete()
        # object.estado = False
        # object.save()
        return redirect('base:agenda')

class AgendaView(ListView):
    model = Agenda
    template_name = "base/agenda/agenda.html"
    context_object_name = "agendas"

class EditarAgendaView(UpdateView):
    model = Agenda
    template_name = "base/agenda/registrar_agenda.html"
    form_class = AgendaForm
    success_url = reverse_lazy('base:agenda')

class EditarHorarioView(UpdateView):
    model = Horario
    template_name = "base/horario/registrar_horario.html"
    form_class = HorarioForm
    success_url = reverse_lazy('base:horario')

class EliminarHorarioView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        horario = Horario.objects.get(id=pk)
        horario.delete()
        # object.estado = False
        # object.save()
        return redirect('base:horario')

class DoctorView(ListView):
    model = Doctor
    template_name = "base/doctor/doctor.html"
    context_object_name = "doctores"
    #queryset = Paciente.objects.filter(estado=False)
   

class EditarDoctorView(UpdateView):
    model = Doctor
    template_name = "base/doctor/registrar_doctor.html"
    form_class = DoctorForm
    success_url = reverse_lazy('base:doctor')

class CrearSignoView(CreateView):
    model = SignoVital
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/signo_vitales/registrar_signo.html"
    form_class = SignoForm
    success_url = reverse_lazy('base:signo')
    context_object_name = "signos"

class SignoView(ListView):
    model = SignoVital
    template_name = "base/signo_vitales/signovitales.html"
    context_object_name = "signos"


class EditarSignoView(UpdateView):
    model = SignoVital
    template_name = "base/signo_vitales/registrar_signo.html"
    form_class = SignoForm
    success_url = reverse_lazy('base:signo')

class EliminarSignoView(DeleteView):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("id")
        signo = SignoVital.objects.get(id=pk)
        signo.delete()
        # object.estado = False
        # object.save()
        return redirect('base:signo')