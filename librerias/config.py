#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import environ
from dotenv import load_dotenv
from os.path import join, dirname
import json
import random, string
import datetime

load_dotenv(join(dirname(__file__), '.env'))

POSTGRE_HOST = environ.get('POSTGRE_HOST')
POSTGRE_DB = environ.get('POSTGRE_DB')
POSTGRE_USER = environ.get('POSTGRE_USER')
POSTGRE_PASS = environ.get('POSTGRE_PASS')


API_CLIMA = environ.get('API_CLIMA')
API_WITH_COORDS = environ.get('API_WITH_COORDS')

