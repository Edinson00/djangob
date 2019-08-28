from django.urls import path
from .views import cargar_inicio, LibroList, LibroCreate, LibroUpdate, LibroDelete, LibroDetalle, EjemplarList, EjemplarDelete, EjemplarCreate

urlpatterns = [
    path('', cargar_inicio, name = 'inicio'),
    path('libros/', LibroList.as_view(), name = 'listar_libros'),
    path('libros/nuevo/', LibroCreate.as_view(), name = 'nuevo_libro'),
    path('libros/editar/<int:pk>', LibroUpdate.as_view(), name = 'editar_libro'),
    path('libros/eliminar/<int:pk>', LibroDelete.as_view(), name = 'borrar_libro'),
    path('libros/detalle/<int:pk>', LibroDetalle.as_view(), name = 'detalle_libro'),
    path('libros/ejemplar', EjemplarList.as_view(), name = 'ejemplar_libro'),
    path('libros/ejemplar/eliminar/<int:pk>', EjemplarDelete.as_view(), name = 'eliminar_ejemplar'),
    path('libros/ejemplar/nuevo/', EjemplarCreate.as_view(), name = 'crear_ejemplar'),


]