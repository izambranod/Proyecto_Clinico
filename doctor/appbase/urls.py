from django.contrib import admin
from django.urls import path
from appbase.views import CrearPacienteView, PacienteView, EditarPacienteView, EliminarPacienteView, CrearDoctorView, CrearHorarioView
from django.conf import settings
app_name = "base"
urlpatterns = [
    path('crear_paciente/', CrearPacienteView.as_view(), name='crear_paciente'),
    path('paciente/', PacienteView.as_view(), name='paciente'),
    path('editar_paciente/<int:pk>/',
         EditarPacienteView.as_view(), name='editar_paciente'),
    path('eliminar_paciente/<int:pk>/',
         EliminarPacienteView.as_view(), name='eliminar_paciente'),
    path('crear_doctor/', CrearDoctorView.as_view(), name='crear_doctor'),
    path('crear_horario/', CrearHorarioView.as_view(), name='crear_horario'),

]
