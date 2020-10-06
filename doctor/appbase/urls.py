from django.contrib import admin
from django.urls import path
from appbase.views import CrearPacienteView, PacienteView, EditarPacienteView, EliminarPacienteView, CrearDoctorView, CrearHorarioView, CrearAgendaView, DoctorView, EditarDoctorView, AgendaView, EditarAgendaView, HorarioView, EditarHorarioView, CrearSignoView, SignoView, EditarSignoView, EliminarDoctorView, EliminarAgendaView, EliminarHorarioView, EliminarSignoView
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
    path('doctor/', DoctorView.as_view(), name='doctor'),
    path('agenda/', AgendaView.as_view(), name='agenda'),
    path('horario/', HorarioView.as_view(), name='horario'),
    path('signo/', SignoView.as_view(), name='signo'),
    path('crear_horario/', CrearHorarioView.as_view(), name='crear_horario'),
    path('crear_agenda/', CrearAgendaView.as_view(), name='crear_agenda'),
    path('editar_doctor/<int:pk>/',
         EditarDoctorView.as_view(), name='editar_doctor'),
    path('editar_agenda/<int:pk>/',
         EditarAgendaView.as_view(), name='editar_agenda'),
    path('editar_horario/<int:pk>/',
         EditarHorarioView.as_view(), name='editar_horario'),
    path('crear_signo/', CrearSignoView.as_view(), name='crear_signo'),
    path('editar_signo/<int:pk>/',
         EditarSignoView.as_view(), name='editar_signo'),
    path('eliminar_doctor/<int:pk>/',
         EliminarDoctorView.as_view(), name='eliminar_doctor'),
     path('eliminar_agenda/<int:pk>/',
         EliminarAgendaView.as_view(), name='eliminar_agenda'),
     path('eliminar_horario/<int:pk>/',
         EliminarHorarioView.as_view(), name='eliminar_horario'),
    path('eliminar_signo/<int:pk>/',
         EliminarSignoView.as_view(), name='eliminar_signo'),
]
