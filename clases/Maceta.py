#!/usr/bin/env python
# -*- coding: utf-8 -*-
from librerias.decorador import cursor_adapter
from clases.Muro         import Muro
from flask import jsonify
from datetime import datetime


class Maceta(Muro):
    def __init__(self,id_maceta=None,estado_sustrato=None,habilitada=True,estado_maceta=None,id_muro=None,comuna=None,direccion=None,habilitado=True):
        Muro.__init__(self,id_muro,comuna,direccion,habilitado)
        self.id_maceta = id_maceta
        self.estado_sustrato = estado_sustrato
        self.habilitada = habilitada
        self.estado_maceta = estado_maceta
        self.id_muro = id_muro

    @cursor_adapter
    def crear_maceta(self,cursor):
        query_existe = """SELECT * FROM  muro where id_muro = %s """
        cursor.execute(query_existe,(self.id_muro,))
        existe = cursor.fetchone()
        if not existe:
            return jsonify({
                'glosa':'el muro en el cual desea agregar maceta no existe o esta deshabilitado',
            }),400
        query = """INSERT INTO maceta (id_muro,estado_sustrato,habilitada,estado_maceta) VALUES (%s,%s,%s,%s) RETURNING id_maceta """
        cursor.execute(query,(self.id_muro,self.estado_sustrato,self.habilitada,self.estado_maceta))
        id_maceta = cursor.fetchone()['id_maceta']
        query = """INSERT INTO variables_algoritmo (id_maceta) values (%s)"""
        cursor.execute(query,(id_maceta,))
        return jsonify({
            'glosa':'muro creado con exito',
            'id':id_maceta
        }),201

    @cursor_adapter
    def listar_macetas(self,cursor,muros):
        print (muros)
        if muros == 'all':
            print ('aca')
            query = """SELECT * FROM muro"""
            cursor.execute(query)
            data = cursor.fetchall()
            query_macetas = """SELECT * FROM maceta """
            cursor.execute(query_macetas)
        else:
            query = """SELECT * FROM muro where id_muro in %s """
            cursor.execute(query,(tuple(muros),))
            data = cursor.fetchall()
            query_macetas = """SELECT * FROM maceta where habilitada = True and id_muro in %s """
            cursor.execute(query_macetas,(tuple(muros),))
        macetas = {}
        for k in cursor.fetchall():
            if k['id_muro'] not in macetas:
                macetas[k['id_muro']] = [
                    {
                        'id':k['id_maceta'],
                        'estado_sustrato':k['estado_sustrato'],
                        'estado_maceta':k['estado_maceta'],
                        'habilitada':k['habilitada']
                    }
                ]
            else:
                macetas[k['id_muro']].append(
                    {
                        'id':k['id_maceta'],
                        'estado_sustrato':k['estado_sustrato'],
                        'estado_maceta':k['estado_maceta'],
                        'habilitada':k['habilitada']
                    }
                )
        for x in data:
            if x['id_muro'] in macetas:
                x['macetas'] = macetas[x['id_muro']]
            else:
                x['macetas'] = []
        if not data:
            return jsonify({
                'glosa':'Listado de macetas',
                'data':[]
            }),204
        return jsonify({
            'glosa':'Listado de macetas',
            'data':data
        }),200

    @cursor_adapter
    def agregar_hora_regadio(self,cursor,hora):
        query = """UPDATE variables_algoritmo set hora_riego = %s where id_maceta = %s """
        cursor.execute(query,(hora,self.id_maceta))
        return jsonify({
            'glosa':'Horario de regadio para la maceta con exito'
        }),200
    @cursor_adapter
    def regar_maceta(self,cursor,tiempo,cantidad):
        fecha = datetime.now()
        query = """INSERT INTO bitacora_regadio(id_maceta,fecha,cantidad_riego,tiempo_riego,tipo_riego) VALUES (%s,%s,%s,%s,'Manual')"""
        cursor.execute(query,(self.id_maceta,fecha,cantidad,tiempo))
        return jsonify({
            'glosa':'riego para la maceta con exito'
        }),200
    @cursor_adapter
    def deshabilitar_maceta(self,cursor):
        query = """SELECT * FROM maceta where id_maceta = %s """
        cursor.execute(query,(self.id_maceta,))
        data = cursor.fetchall()
        if not data:
            return jsonify({
                'glosa':'la maceta en el cual desea deshabilitar no existe '
            }),400
        query = """UPDATE maceta set habilitada = False where id_maceta = %s"""
        cursor.execute(query,(self.id_maceta,))
        return jsonify({
            'glosa':'Maceta deshabilitada con exito'
        }),202
    
