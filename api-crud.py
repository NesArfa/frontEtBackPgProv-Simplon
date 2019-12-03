"""
python 3.7

API 1 --  to read, update and delete the SQL database

John Armitage, Axel Alves 3/12/2019
"""

import sqlalchemy
import json
import os
import base64
from flask import *
from flask_cors import CORS
from os import path

from config import DATABASE_URI
from model import Base, compte

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
s = Session()

app = Flask(__name__)

# _______________ Fonctions ____________
def readData(numb):
    query = s.query(compte).filter_by(ID=numb)
    return query.all()


def putData(data):
    sqldata = json.loads(data)
    tableEntry = compte(
                ID=int(sqldata["ID"]),
                Nom=sqldata["Nom"],
                Owner=sqldata["Owner"],
                User=sqldata["User"],
                Password=sqldata["Password"],
                Namespace=sqldata["Namespace"],
            )
    s.add(tableEntry)
    s.commit()


# _______________ ROUTES _______________

@app.route('/v1/hello-world')
#CORS(app)
def hello_world():
    return 'Hello World!'


@app.route('/data/<articleid>', methods=['GET'])
#CORS(app)
def parse_reqget(articleid):
    # Votre fonction pour lire les data d'un fichier
    data = readData(articleid)
    return data


@app.route('/data', methods=['POST'])
#CORS(app)
def parse_reqpost():
    data = request.data  # Le payload de votre requete
    result = putData(data)
    return result


if __name__ == '__main__':
    app.run()
    #app.run("0.0.0.0")
