#!/usr/bin/env python
# -*- coding: utf-8 -*-
from librerias.decorador import cursor_adapter
from flask import jsonify
import json


class Muro:

    def __init__(self,id_muro=None,comuna=None,direccion=None,habilitado=True):
        self.id_muro = id_muro
        self.comuna = comuna
        self.direccion = direccion
        self.habilitado = habilitado

    @cursor_adapter
    def crear_muro(self,cursor):
        query = """INSERT INTO muro (comuna,direccion,habilitado) VALUES (%s,%s,%s) RETURNING id_muro"""
        cursor.execute(query,(self.comuna,self.direccion,self.habilitado))
        id_muro = cursor.fetchone()['id_muro']
        return jsonify({
            'glosa':'muro creado con exito',
            'id':id_muro
        }),201
    
    @cursor_adapter
    def listar_muros(self,cursor,comunas=None,all=False):
        if all:
            query = """SELECT * FROM muro """
            cursor.execute(query)
            response = [{'id':k['id_muro'],'comuna':k['comuna'],'direccion':k['direccion'],'habilitado':k['habilitado']} for k in cursor.fetchall()]
            if response:
                return jsonify(
                    {
                        'glosa':'listado de muros',
                        'data':response
                    }
                ),200
            else:
                return jsonify(
                    {
                        'glosa':'sin contenido de muros'
                    }
                ),204
        query = """SELECT * FROM muro where comuna in %s """
        cursor.execute(query,(tuple(comunas),))
        response = [{'id':k['id_muro'],'comuna':k['comuna'],'direccion':k['direccion']} for k in cursor.fetchall()]
        if response:
            return jsonify(
                {
                    'glosa':'listado de muros',
                    'data':response
                }
            ),200
        else:
            return jsonify(
                {
                    'glosa':'sin contenido de muros'
                }
            ),204

    @cursor_adapter
    def modificar_muro(self,cursor):
        query = """SELECT * FROM muro where id_muro =  %s """
        cursor.execute(query,(self.id_muro,))
        data = cursor.fetchone()
        if not data:
            return jsonify({
                'glosa':'el muro a editar no eixste',
            }),400

        query = """update muro set comuna=%s,direccion=%s where id_muro = %s"""
        cursor.execute(query,(self.comuna,self.direccion,self.id_muro))

        return jsonify({
            'glosa':'muro editado con exito',
        }),200

    @cursor_adapter
    def deshabilitar_muro(self,cursor):
        query = """SELECT * FROM muro where id_muro =  %s """
        cursor.execute(query,(self.id_muro,))
        data = cursor.fetchone()
        if not data:
            return jsonify({
                'glosa':'el muro a deshabilitado no eixste',
            }),400
            
        query = """update muro set habilitado=%s where id_muro = %s"""
        cursor.execute(query,(False,self.id_muro))
        return jsonify({
            'glosa':'muro deshabilitado con exito',
        }),202

    @cursor_adapter
    def habilitar_muro(self,cursor):
        query = """SELECT * FROM muro where id_muro =  %s """
        cursor.execute(query,(self.id_muro,))
        data = cursor.fetchone()
        if not data:
            return jsonify({
                'glosa':'el muro para habilitar no eixste',
            }),400
            
        query = """update muro set habilitado=%s where id_muro = %s"""
        cursor.execute(query,(True,self.id_muro))
        return jsonify({
            'glosa':'muro habilitado con exito',
        }),200