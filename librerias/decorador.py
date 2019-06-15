import psycopg2
import psycopg2.extras
import librerias.config as cf
import traceback
from flask import jsonify




# import random, string
posthost = cf.POSTGRE_HOST
postdbname = cf.POSTGRE_DB
postuser = cf.POSTGRE_USER
postpass = cf.POSTGRE_PASS


def postgre_Connect():
    connect_str = "dbname='{}' user='{}' host='{}' password='{}'".format(
        postdbname, postuser, posthost, postpass)
    return psycopg2.connect(connect_str)


def cursor_adapter(f):
    def with_connection_(self,*args, **kwargs):
        # or use a pool, or a factory function...
        cnn = postgre_Connect()
        
        try:
            with cnn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.itersize = 1000
                rv = f(self,cursor, *args, **kwargs)
        except Exception as e:
            cnn.rollback()
            
            err = f.__name__
            err += ' ERROR: ' + str(e)
            print (traceback.format_exc())
            desc = str(err) + ", problema: " + str(e)
            rv =  jsonify({
                "glosa":desc
            }),500
        else:
            cnn.commit() # or maybe not
        finally:
            cnn.close()
        return rv
    return with_connection_