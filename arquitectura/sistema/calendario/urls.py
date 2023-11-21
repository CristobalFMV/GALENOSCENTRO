from django.urls import path
from .views import administrador, home, registrarUsuario,eliminarUsuario,editarUsuario, editUsuario,calendario,secretaria,paciente,crearUsuario
urlpatterns = [
    path('', home, name="home"),
    path('administrador', administrador,name="administrador"),
    path('registrarUsuario/',registrarUsuario,name="registrarUsuario"),
    path('eliminarUsuario/<rut>',eliminarUsuario,name="eliminarUsuario"),
    path('editarUsuario/<rut>',editarUsuario,name="editarUsuario"),
    path('editUsuario/',editUsuario,name="editUsuario"),
    path('calendario',calendario, name="calendario"),
    path('secretaria', secretaria, name="secretaria"),
    path('paciente', paciente, name="paciente"),
    path('crearUsuario/',crearUsuario,name="crearUsuario")    
]

