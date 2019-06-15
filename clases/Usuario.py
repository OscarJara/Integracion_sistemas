#!/usr/bin/env python
# -*- coding: utf-8 -*-
from librerias.decorador import cursor_adapter
from flask import jsonify
# import uuid4

class Usuario:

    def __init__(self,nombre=None,apellido=None,cargo=None,usuario=None,password=None,id_user=None):
        self.id_user = id_user
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.usuario = usuario
        self.password = password

    @cursor_adapter
    def logeo(self,cursor):
        query = """SELECT * FROM usuario where usuario = %s and password = %s """
        cursor.execute(query,(self.usuario,self.password))
        response = False
        response_json = {}
        for data in cursor.fetchall():
            response = True
            response_json = {
                    'id':data['id_usuario'],
                    'nombre':data['nombre'],
                    'apellido':data['apellido'],
                    'cargo':data['cargo'],
                    'usuario':data['usuario']
                }
        if response:
            return jsonify({
                'glosa':'usuario logueado',
                'id':response_json['id'],
                'nombre':response_json['nombre'],
                'apellido':response_json['apellido'],
                'cargo':response_json['cargo'],
                'usuario':response_json['usuario']
            }),200
        else:
            return jsonify({
                'glosa':'Usuario o contraseña incorrecta',
                'data':[]
            }),400
    @cursor_adapter
    def add_user(self,cursor):
        query = """SELECT * FROM usuario where usuario = %s"""
        cursor.execute(query,(self.usuario,))
        existe = cursor.fetchone()
        if existe:
            return jsonify({
            'glosa':'usuario existente'
        }),400
        query = """INSERT INTO usuario (nombre,apellido,cargo,usuario,password) VALUES (%s,%s,%s,%s,%s) """
        cursor.execute(query,(self.nombre,self.apellido,self.cargo,self.usuario,self.password))

        return jsonify({
            'glosa':'usuario creado con exito'
        }),201

    @cursor_adapter
    def list_user(self,cursor):
        query = """SELECT * FROM usuario where activado = 1"""
        cursor.execute(query)
        response = []
        for data in cursor.fetchall():
            response.append(
                {
                    'id':data['id_usuario'],
                    'nombre':data['nombre'],
                    'apellido':data['apellido'],
                    'cargo':data['cargo'],
                    'usuario':data['usuario']
                }
            )
        if response:
            return jsonify({
                'glosa':'lista de usuarios',
                'data':response
            }),200
        else:
            return jsonify({
                'glosa':'lista de usuarios',
                'data':[]
            }),204

    @cursor_adapter
    def update_user(self,cursor):
        query = """SELECT * FROM usuario where id_usuario = %s"""
        cursor.execute(query,(self.id_user,))
        existe = cursor.fetchone()
        if not existe:
            return jsonify({
            'glosa':'usuario no existente'
        }),400
        query = """update usuario set nombre=%s,apellido=%s,cargo=%s,usuario=%s,password=%s where id_usuario = %s """
        cursor.execute(query,(self.nombre,self.apellido,self.cargo,self.usuario,self.password,self.id_user))

        return jsonify({
            'glosa':'usuario editado con exito'
        }),200
    @cursor_adapter
    def delete_user(self,cursor):
        query = "DELETE FROM usuario where id_usuario=%s"
        cursor.execute(query,(self.id_user,))
        return jsonify({
            'glosa':'usuario eliminado con exito'
        }),202
