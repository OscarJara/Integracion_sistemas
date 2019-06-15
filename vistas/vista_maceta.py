from clases.Maceta import Maceta


import base64
import librerias.config as cf


def crear_muro(request):
    comuna = request.json['comuna']
    direccion = request.json['direccion']
    muro = Maceta(
        comuna=comuna,
        direccion=direccion
    )
    return muro.crear_muro()

def listar_macetas(comunas):
    if comunas == 'all':
        muro = Maceta()
        return muro.listar_muros(all=True)
    comunas = comunas.split(',')
    muro = Maceta()
    return muro.listar_muros(comunas=comunas)

def modificar_muro(request):
    id = request.json['id']
    comuna = request.json['comuna']
    direccion = request.json['direccion']
    muro = Maceta(
            id_muro=id,
            comuna=comuna,
            direccion=direccion,
        )
    return muro.modificar_muro()

def eliminar_muro(request):
    id = request.json['id']
    muro = Maceta(
        id_muro=id
    )
    return muro.deshabilitar_muro()

def habilitar_muro(request):
    id = request.json['id']
    muro = Maceta(
        id_muro=id
    )
    return muro.habilitar_muro()

def crear_maceta(request):
    id_muro = request.json['id_muro']
    estado_sustrato = request.json['estado_sustrato']
    estado_maceta = request.json['estado_maceta']
    maceta = Maceta(
        id_muro=id_muro,
        estado_sustrato=estado_sustrato,
        estado_maceta=estado_maceta
    )
    return maceta.crear_maceta()

def listado_macetas(muros):
    maceta = Maceta()
    if muros == 'all':
        return maceta.listar_macetas(muros)
    muros = muros.split(',')
    
    return maceta.listar_macetas(muros)

def deshabilitar_maceta(request):
    id = request.json['id']
    maceta = Maceta(id_maceta=id)
    return maceta.deshabilitar_maceta()

def agregar_hora_regadios(request):
    id = request.json['id']
    hora = request.json['hora']
    maceta = Maceta(id_maceta=id)
    return maceta.agregar_hora_regadio(hora)

def regar(request):
    id = request.json['id']
    tiempo = request.json['tiempo']
    cantidad = request.json['cantidad']
    maceta = Maceta(id_maceta=id)
    return maceta.regar_maceta(tiempo,cantidad)