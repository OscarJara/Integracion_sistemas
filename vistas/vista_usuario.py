from clases.Usuario import Usuario


import base64
import librerias.config as cf


def crear_usuario(request):
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    cargo = request.json['cargo']
    usuario = request.json['usuario']
    password = request.json['password']
    user = Usuario(
        nombre,
        apellido,
        cargo,
        usuario,
        password
    )
    return user.add_user()

def listar_usuario():
    user = Usuario()
    return user.list_user()

def logueo(request):
    usuario = request.json['usuario']
    password = request.json['password']
    user = Usuario(
        usuario=usuario,
        password=password
    )
    return user.logeo()

def modificar_usuario(request):
    id_user = request.json['id']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    cargo = request.json['cargo']
    usuario = request.json['usuario']
    password = request.json['password']
    user = Usuario(
        nombre,
        apellido,
        cargo,
        usuario,
        password,
        id_user
    )
    return user.update_user()

def eliminar_usuario(request):
    id_user = request.json['id']
    user = Usuario(id_user=id_user)
    return user.delete_user()