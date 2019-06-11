#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask,jsonify,request
from flask_cors import CORS

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

if __name__ == "__main__":
    app.run(debug=True) 