#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask,jsonify,request
from flask_cors import CORS



### VISTAS
from vistas  import vista_usuario    as usuario
from vistas  import vista_maceta     as maceta
### VISTAS


app = Flask(__name__)
CORS(app)


@app.route('/',methods=['GET'])
def inicial():
    return jsonify(
        {
            'estado':200,
            'glosa':'endpoint inicial ok'
        }
    ),200


@app.route('/usuario',methods=['POST'])
def add_user():
    return usuario.crear_usuario(request)


@app.route('/usuario',methods=['GET'])
def list_user():
    return usuario.listar_usuario()

@app.route('/usuario',methods=['PUT'])
def modificar_user():
    return usuario.modificar_usuario(request)

@app.route('/usuario',methods=['DELETE'])
def eliminar_user():
    return usuario.eliminar_usuario(request)

@app.route('/login',methods=['POST'])
def login():
    return usuario.logueo(request)


@app.route('/muro',methods=['POST'])
def crear_muro():
    return maceta.crear_muro(request)

@app.route('/muro/<comunas>',methods=['GET'])
def listar_muro(comunas):
    return maceta.listar_macetas(comunas)

@app.route('/muro',methods=['PUT'])
def modificar_mro():
    return maceta.modificar_muro(request)

@app.route('/muro',methods=['DELETE'])
def eliminar_mro():
    return maceta.eliminar_muro(request)
@app.route('/muro-habilitar',methods=['POST'])
def habilitando_muro():
    return maceta.habilitar_muro(request)

@app.route('/maceta',methods=['POST'])
def crear_macet():
    return maceta.crear_maceta(request)

@app.route('/maceta/<muros>',methods=['GET'])
def listado_macetas(muros):
    return maceta.listado_macetas(muros)

@app.route('/maceta',methods=['DELETE'])
def deshabilitar_macetas():
    return maceta.deshabilitar_maceta(request)

@app.route('/hora-regadio',methods=['POST'])
def hora_regadio():
    return maceta.agregar_hora_regadios(request)

@app.route('/regar',methods=['POST'])
def regar_manual():
    return maceta.regar(request)
if __name__ == "__main__":
    app.run(debug=True) 