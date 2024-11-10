from email.policy import default

from django import forms
# Create your models here.
generos_agregados= [
    (None,"seleccione"),
    ("M","Masculino"),
    ("F","Femenino"),
]
usuarios_new = []
class UsuariosForm(forms.Form):
    nombre = forms.CharField(max_length=50,label="Nombre",required=True,widget=forms.TextInput(attrs={'class': 'form-control','pattern': '[A-Za-z]+','title': 'El nombre solo debe contener letras.' }))
    cedula = forms.CharField(max_length=10,min_length=10,label="Cedula",required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]+','title': 'La cedula debe contener solo caracteres.' }))
    apellido = forms.CharField(max_length=50,label="Apellido",required=True,widget=forms.TextInput(attrs={'class': 'form-control','pattern': '[A-Za-z]+', 'title': 'El apellido solo debe contener letras.' }))
    email = forms.EmailField(label="Email ",required=True,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    genero = forms.ChoiceField(choices=generos_agregados,label="Genero",required=True,widget=forms.Select(attrs={'class': 'form-control'}) )
buscado=[
    (None,"seleccione"),
    ("N","Nombre"),
    ("A","Apellido"),
    ("E","Email"),
    ("G","Genero"),
    ("T","Ticket"),
]
ordenado=[
    (None,"seleccione"),
    ("nombre","Nombre"),
    ("apellido","Apellido"),
    ("email","Email"),
    ("ticket","Ticket"),
    ("genero","genero"),
]
class Bucar(forms.Form):
    BC = forms.CharField(max_length=50, label="Buscar",required=False,widget=forms.TextInput(attrs={'class': 'form-control-busqueda'}))
    type_bus = forms.ChoiceField(choices=buscado, label="Busqueda", required=False, widget=forms.Select(attrs={'class': 'form-control-busqueda'}))
    type_or = forms.ChoiceField(choices=ordenado, label="Ordenar", required=False, widget=forms.Select(attrs={'class': 'form-control-busqueda'}))

class ArchivoForm(forms.Form):
    archivo = forms.FileField(label="Archivo")

