from librerias.decorador  import postgre_Connect

import librerias.config as cf
import traceback
import psycopg2
import requests
import json
import copy
import datetime
# FORMULA = (fahrenheit-32) * (5/9)



def cron(cursor):
    URL_CLIMA = cf.API_CLIMA
    response = requests.get(URL_CLIMA)
    if response.status_code == 200:
        response = json.loads(response.content.decode("utf-8"))
        humedad = round(response['currently']['humidity'])
        temperatura = (int(round(response['currently']['temperature']))-32) * (5/9)
        if humedad < 20:
            if temperatura > 1 and temperatura< 40:
                fecha = datetime.datetime.now()
                hora = str(fecha.hour)
                fecha_completa = int(str(fecha.year)+str(fecha.month)+str(fecha.day))
                query = """SELECT * FROM variables_algoritmo where riego_activado= True"""
                cursor.execute(query)
                macetas = cursor.fetchall()
                for data in macetas:
                    if data['hora_riego'] == hora:
                        if data['fecha'] == None or data['fecha'] < fecha_completa:
                            query = """INSERT INTO bitacora_regadio (id_maceta,fecha,cantidad_riego,tiempo_riego,tipo_riego) values (%s,%s,%s,%s,%s)"""
                            cursor.execute(query,(data['id_maceta'],fecha,1,30,'Automatico'))
                            query = """UPDATE variables_algoritmo set fecha = %s where id_maceta = %s """
                            cursor.execute(query,(fecha_completa,data['id_maceta']))

    

if __name__ == "__main__":
    cnn = postgre_Connect()   
    try:
        with cnn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.itersize = 1000
            cron(cursor)
    except Exception as e:
        print (traceback.format_exc())
        cnn.rollback()
    finally:
        cnn.commit()
    