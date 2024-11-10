import io
import json
from django.core import management
from django.http import HttpResponse
from django.db import DatabaseError
from django.shortcuts import render, redirect
from .forms import UsuariosForm, Bucar, ArchivoForm
from .models import Usuario, Archivo
from .clases import  ListaEnlazada, Error, Organizar


# Create your views here.

def index(request):
    vincular = ListaEnlazada()
    mensaje=None
    atendiendo = None
    nodos=""
    try:
        for i in Usuario.objects.all():
            vincular.agregar_usuario(i)
        estados = vincular.listar_usuarios()
        nodos=vincular.listar_usuarios()
    except DatabaseError as e:
        mensaje= f"Hubo un error en la base de datos {e}"
    except AttributeError as e:
        mensaje=f"Hubo un error inenperado {e}"
    except  Exception as e:
        mensaje=f"Hubo un error inesperado {e}"
    else:
        for guardar in estados:
            if guardar.estado == "Atendiendo":
                atendiendo = guardar
                break
    requerido={
        "vincular":nodos ,
        "Atendiendo": atendiendo,
        "Presentar":True,
        "Mensaje":mensaje,
        "Presentar_blo": True,
    }
    return render(request,"modelo1/index.html",requerido)
def formulario(request):
    vincular = ListaEnlazada()
    from_1 = UsuariosForm()
    atendiendo_f = None
    if request.method=="POST":
        form =UsuariosForm(request.POST)
        if form.is_valid():
            ultimo_usuario=None
            for i in Usuario.objects.all():
                ultimo_usuario = i.ticket
            nuevo_tiket = (ultimo_usuario + 1) if ultimo_usuario else 1
            user = Usuario(
            nombre = form.cleaned_data['nombre'],
            apellido = form.cleaned_data['apellido'],
            email = form.cleaned_data['email'],
            genero = form.cleaned_data['genero'],
            cedula = form.cleaned_data['cedula'],
            ticket=nuevo_tiket
            )
            user.save()
    for i in Usuario.objects.all():
        vincular.agregar_usuario(i)
    estados = vincular.listar_usuarios()
    nodos = vincular.listar_usuarios()
    for guardar in estados:
        if guardar.estado == "Atendiendo":
            atendiendo_f = guardar
            break
    requerido = {
        "vincular": nodos,
        "Atendiendo": atendiendo_f,
        "Presentar": True,
        "forms": from_1,
    }
    return render(request,"modelo1/formulario.html",requerido)
def tabla(request):
    vincular = ListaEnlazada()
    mensaje=None
    errores=Error()
    ordenar=Organizar()
    if request.method == "POST":
       form = Bucar(request.POST)
       if form.is_valid():
            b_1=form.cleaned_data['BC']
            b_2=form.cleaned_data['type_bus']
            b_3=form.cleaned_data['type_or']
            if ( b_1 != "" and b_2 != "") or b_3 != "":
                try:
                   if b_1!="" and b_2!="" :
                       if b_2 == "N":
                           if errores.error_1(b_1) is None:
                               for i in Usuario.objects.all():
                                   if b_1.upper() in i.nombre.upper():
                                       vincular.agregar_usuario(i)
                       elif b_2 == "A":
                           if errores.error_1(b_1) is None:
                               for i in Usuario.objects.all():
                                   if b_1.upper() in i.apellido.upper():
                                       vincular.agregar_usuario(i)
                       elif b_2 == "E":
                           if errores.error_2(b_1) is None:
                               for i in Usuario.objects.all():
                                   if b_1.upper() in i.email.upper():
                                       vincular.agregar_usuario(i)
                       elif b_2 == "G":
                           if errores.error_3(b_1) is  None:
                               if b_1.upper() == "FEMENINO":
                                   genero_f_m = "F"
                               else:
                                   genero_f_m = "M"
                               for i in Usuario.objects.all():
                                   if genero_f_m.upper() in i.genero.upper():
                                       vincular.agregar_usuario(i)
                       else:
                           if errores.error_4(b_1) is None:
                               use = Usuario.objects.all()
                               print(use)
                               inico, fin = 0, len(use)
                               while inico < fin:
                                   medio = (inico + fin) // 2
                                   if use[medio].ticket == int(b_1):
                                       vincular.agregar_usuario(use[medio])
                                       break
                                   elif use[medio].id < int(b_1):
                                       inico = medio
                                   else:
                                       fin = medio
                   lista = ordenar.organizar_lis(vincular)
                   if b_3 != "" and b_2 == "" and b_1 == "":
                       for i in Usuario.objects.all():
                           lista.append(i)
                       lista_ordenada = ordenar.quicksort(lista, b_3)
                   elif b_3 != "" and b_2 != "" and b_1 != "":
                      lista_ordenada = ordenar.quicksort(lista, b_3)
                   elif b_3 == "" and b_2 != "" and b_1 != "":
                       lista_ordenada = vincular.listar_usuarios()
                   else:
                       raise Exception("Llene todo los campos o solo el de ordenar")
                except ValueError:
                    mensaje = "Por favor ingrese un numero, Ejemplo:10"
                except Exception as e:
                    mensaje = f"{e}"
                else:
                    contenido = {"vincular": lista_ordenada,
                                 "Presentar": False,
                                 "busqueda": Bucar(),
                                 "Mensaje": mensaje,
                                 }
                    return render(request, "modelo1/tabla.html", contenido, )
    else:
        for i in Usuario.objects.all():
            vincular.agregar_usuario(i)
    contenido={"vincular": vincular.listar_usuarios(),
               "Presentar": False,
               "busqueda": Bucar(),
               "Mensaje":mensaje,
               }
    return render(request, "modelo1/tabla.html",contenido,)
def siguiente(request):
    vincular = ListaEnlazada()
    for i in Usuario.objects.all():
        vincular.agregar_usuario(i)
    estados = vincular.listar_usuarios()
    for guardar in estados:
        if guardar.estado == "Atendiendo":
            data_bs = Usuario.objects.get(id=guardar.id)
            data_bs.estado = "Atendido"
            data_bs.save()
        elif guardar.estado == "Espera":
            data_bs = Usuario.objects.get(id=guardar.id)
            data_bs.estado = "Atendiendo"
            data_bs.save()
            break
    return redirect("index")
def borrar(request):
    Usuario.objects.all().delete()
    return redirect("index")
def borrar_1(request,id_1):
    use=Usuario.objects.all()
    inico,fin = 0,len(use)
    while inico<fin:
        medio = (inico + fin) // 2
        if use[medio].id == id_1:
            use_obj = Usuario.objects.get(id=use[medio].id)
            use_obj.delete()
            break
        elif use[medio].id < id_1:
            inico=medio
        else:
            fin=medio
    return redirect("tabla")
def editar(request,id_1):
    form=UsuariosForm()
    if request.method == "POST":
        from_2 = UsuariosForm(request.POST)
        if from_2.is_valid():
            user = Usuario.objects.get(id=id_1)
            user.nombre = from_2.cleaned_data['nombre']
            user.apellido = from_2.cleaned_data['apellido']
            user.email = from_2.cleaned_data['email']
            user.genero = from_2.cleaned_data['genero']
            user.save()
    return render(request,"modelo1/editar.html",{"forms": form,"Presentar":False,"id":id_1})
def descargar(request):
    usuarios = Usuario.objects.all()

    try:
       if len(usuarios)>0:
           buffer = io.StringIO()
           management.call_command('dumpdata', 'modelo1.Usuario', stdout=buffer)
           nombre_archivo = "tiket.json"
           res = HttpResponse(buffer.getvalue(), content_type='application/json')
           res['Content-Disposition'] = f'attachment; filename={nombre_archivo}'
           return res
       else:
           raise ValueError("La tabla esta vacia")
    except Exception as e:
        mensaje={e}
        contenido={
            "vincular": None,
            "Atendiendo": None,
            "Presentar": True,
            "Mensaje": mensaje,
        }
        return render(request,"modelo1/index.html",contenido)

def cargar(request):
    mensaje=None
    try:
        if request.method == "POST":
            fo = ArchivoForm(request.POST,request.FILES)
            if fo.is_valid():
               arc= fo.cleaned_data.get('archivo')
               if arc.content_type != 'application/json':
                   raise ValueError("Solo se permiten archivos JSON.")
               else:
                   arc_2=fo.cleaned_data['archivo']
                   cargado=Archivo(
                       archivo=arc_2 )
                   cargado.save()
    except Exception as e:
        mensaje= f"{e}"
    else:
       mensaje=None
    finally:
        vincular = ListaEnlazada()
        atendiendo = None
        nodos = ""
        form = ArchivoForm()
        for i in Usuario.objects.all():
            vincular.agregar_usuario(i)
        estados = vincular.listar_usuarios()
        nodos = vincular.listar_usuarios()
        for guardar in estados:
            if guardar.estado == "Atendiendo":
                atendiendo = guardar
                break
        requerido = {
            "vincular": nodos,
            "Atendiendo": atendiendo,
            "Presentar": True,
            "form": form,
            "Mensaje": mensaje,
            "Archivo": Archivo.objects.all(),
        }

        return render(request,"modelo1/archivo.html",requerido)
def mostrar_json(request,id_1):
    archivos = Archivo.objects.all()
    data = None
    if archivos.exists():
        archivo = archivos.get(id=id_1)
        with archivo.archivo.open('r') as f:
            data = json.load(f)
    return render(request, 'modelo1/ver.html', {'data': data})

def subir_tabla(request,id_1):
    archivos = Archivo.objects.all()
    user_1=Usuario.objects.all()
    mensajess=None
    try:
       if len(user_1) == 0:
           if archivos.exists():
               archivo = archivos.get(id=id_1)
               with archivo.archivo.open('r') as f:
                   data = json.load(f)
               for i in data:
                   if "fields" in i and "nombre" in i["fields"]:
                       user = Usuario(
                           nombre=i["fields"]["nombre"],
                           apellido=i["fields"]["apellido"],
                           email=i["fields"]["email"],
                           genero=i["fields"]["genero"],
                           estado=i["fields"]["estado"],
                           ticket=i["fields"]["ticket"],
                           cedula=i["fields"]["cedula"],

                       )
                       user.save()
       else:
           raise ValueError("Ya existe una tabla")
    except Exception as e:
        mensajess= f"{e}"

    vincular = ListaEnlazada()
    atendiendo = None
    archivos = Archivo.objects.all()
    for i in Usuario.objects.all():
        vincular.agregar_usuario(i)
    estados = vincular.listar_usuarios()
    nodos = vincular.listar_usuarios()
    for guardar in estados:
        if guardar.estado == "Atendiendo":
            atendiendo = guardar
            break
    requerido = {
        "vincular": nodos,
        "Atendiendo": atendiendo,
        "Presentar": True,
        "archivos": archivos,
        "mensaje": mensajess,
    }
    return render(request,"modelo1/tablas_c.html",requerido)

def tablas_c(request):
    vincular = ListaEnlazada()
    atendiendo = None
    archivos = Archivo.objects.all()
    for i in Usuario.objects.all():
        vincular.agregar_usuario(i)
    estados = vincular.listar_usuarios()
    nodos = vincular.listar_usuarios()
    for guardar in estados:
        if guardar.estado == "Atendiendo":
            atendiendo = guardar
            break
    requerido = {
        "vincular": nodos,
        "Atendiendo": atendiendo,
        "Presentar": True,
        "archivos": archivos,
        "mensaje": None,
    }

    return render(request,"modelo1/tablas_c.html",requerido)

def borrar_1_tabla(request,id_1):
    arc=Archivo.objects.all()
    inico,fin = 0,len(arc)
    while inico<fin:
        medio = (inico + fin) // 2
        if arc[medio].id == id_1:
            arc_obj = Archivo.objects.get(id=arc[medio].id)
            arc_obj.delete()
            break
        elif arc[medio].id < id_1:
            inico=medio
        else:
            fin=medio
    return redirect("tablas_c")