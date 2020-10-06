from django import forms
from django.db.models import fields
from .models import Paciente, Doctor, Horario, Agenda, SignoVital


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        # fields = ('nombre', 'apellido', 'cedula')
        # label = {
        #     'nombre': 'Nombres',
        #     'apellido': 'Apellidos',
        #     'cedula': 'Cedula'
        # }

        # fields = ('cedula','nombre','apellido','nacimiento','sexo','civil','profesion','titulo','provincia','ciudad','direccion','telefono','email','foto','sangre','hijos','estado')
        # label = {'descripcion': 'Producto', 'precio': 'Precio', 'stock': 'Stock', 'iva': 'Iva'}


        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Ingrese su numero de cedula'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Ingrese sus dos nombres'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Ingrese sus apellidos'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'dd/mm/aaaa', 'type': 'date'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'civil': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'profesion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'titulo': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Ingrese su dirección actual'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Ingrese su número telefónico'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Ingrese su dirección de correo electrónico'
                }
            ),
            'foto': forms.FileInput(
                 attrs={
                    'class': 'form-control-file'
                }
            ),
            'sangre': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'hijos': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            )
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        # fields = ('nombre', 'apellido', 'cedula')
        # label = {
        #     'nombre': 'Nombres',
        #     'apellido': 'Apellidos',
        #     'cedula': 'Cedula'
        # }

        # fields = ('cedula','nombre','apellido','nacimiento','sexo','civil','profesion','titulo','provincia','ciudad','direccion','telefono','email','foto','sangre','hijos','estado')
        # label = {'descripcion': 'Producto', 'precio': 'Precio', 'stock': 'Stock', 'iva': 'Iva'}


        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Ingrese su numero de cedula'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Ingrese sus dos nombres'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Ingrese sus apellidos'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'dd/mm/aaaa', 'type': 'date'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'civil': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'profesion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'titulo': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Ingrese su dirección actual'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Ingrese su número telefónico'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Ingrese su dirección de correo electrónico'
                }
            ),
            'foto': forms.FileInput(
                 attrs={
                    'class': 'form-control-file'
                }
            ),
            'consultorio': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Ingrese el nombre de su consultorio'
                }
            ),
            'lugar': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Direccion del consultorio'
                }
            ),
            'logo': forms.FileInput(
                 attrs={
                    'class': 'form-control-file'
                }
            ),
            'horario': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'registro': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Registro medico'
                }
            ),
            'duracion': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            )
        }

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'
        widgets = {
            'dia': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Dia'
                }
            ),
            'desde': forms.TimeInput(
               attrs={'class':'form-control', 
                       'placeholder':'hh:mm', 'type': 'time'
                       }
            ),
            'hasta': forms.TimeInput(
                attrs= {'class': 'form-control',
                       'placeholder': 'hh:mm', 'type': 'time'
                }
            ),
           'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }     
            ),

        }

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'
        widgets = {
            'paciente': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fecha': forms.DateInput(
               attrs={'class':'form-control', 'type':'date'}
            ),
            'hora': forms.TimeInput(
                attrs= {'class': 'form-control',
                       'placeholder': 'hh:mm', 'type': 'time'
                }
            ),
            'motivo': forms.TextInput(
                attrs= {'class': 'form-control',
                       'placeholder': 'Motivo de la consulta'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs= {'class': 'form-check-input',
                }      
            ),

        }

class SignoForm(forms.ModelForm):
    class Meta:
        model = SignoVital
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput (
                attrs= {
                    'class': 'form-control', 'placeholder': 'Signo vital'
                }
            ),
            'rango1': forms.NumberInput (
                attrs= {
                    'class': 'form-control', 'placeholder': '0.00'
                }
            ),
            'rango2': forms.NumberInput (
                attrs= {
                    'class': 'form-control', 'placeholder': '0.00'
                }
            ),
            'medida': forms.TextInput (
                attrs= {
                    'class': 'form-control'
                }
            ),
             'imagen': forms.FileInput(
                 attrs={
                    'class': 'form-control-file'
                }
            ),
             'estado': forms.CheckboxInput(
                attrs= {'class': 'form-check-input',
                }  
            ),
        }

