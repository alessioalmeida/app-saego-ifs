# -*- coding: UTF-8 -*-
from os import getenv
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

try:
    db_uri = f'mongodb+srv://{getenv("USR")}:{getenv("PWD")}@{getenv("HST")}'
    mongo_client = MongoClient(db_uri)

except Exception as e:
    raise Exception(f'Erro de conexão com banco de dados: {str(e)}') from e
