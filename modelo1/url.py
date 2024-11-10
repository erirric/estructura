
from django.urls import path
from . import views
urlpatterns = [
     #path("",views.saludo),
     path("",views.index,name="index"),
     path("formulario/",views.formulario,name="formulario"),
     path("tabla/",views.tabla,name="tabla"),
     path("siguiente/",views.siguiente,name="siguiente"),
     path("borrar/",views.borrar,name="borrar"),
     path("borrar_1/<int:id_1>/",views.borrar_1,name="borrar_1"),
     path("editar/<int:id_1>",views.editar,name="editar"),
     path("descarga/",views.descargar,name="descarga"),
     path("cargar/",views.cargar,name="cargar"),
     path('mostrar-json/<int:id_1>', views.mostrar_json, name='mostrar_json'),
     path('subir_tabla/<int:id_1>', views.subir_tabla, name='subir_tabla'),
     path('tablas_c/', views.tablas_c, name='tablas_c'),
     path('borrar_1_tabla/<int:id_1>', views.borrar_1_tabla, name='borrar_1_tabla'),
]


