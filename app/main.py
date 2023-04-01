import os
import logging 
import requests

from fastapi import FastAPI
from dotenv import load_dotenv
from utils import *
from qa_menuboard import *

# Configurar el log
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('DevTools_log.log', mode='w')
    ]
)

# Leer variables de entorno
PATH_PRECIOS_BK = os.getenv("PATH_PRECIOS_BK")
PATH_PRECIOS_MCD = os.getenv("PATH_PRECIOS_MCD")

app = FastAPI()

logging.info('===== SERVICE INIT ======')

@app.get("/")
async def root():
    return {"message": "Hola amigo " + PATH_PRECIOS_BK}


#======== MUSEOS ==========
@app.get("/museos/")
def museos():
    response = requests.get("https://www.cultura.gob.ar/api/v2.0/museos/?format=json")
    #response = ""
    return {"response": response.json()}

#======== MCD ==========
@app.get("/mcd/read")
def mcdRead():
    logging.debug("====> mcd: {}".format(mcdRead.__name__))    
    return mbMcdReadPrice()

@app.get("/mcd/modify")
def mcdModify():
    logging.debug("====> mcd: {}".format(mcdRead.__name__))
    return mbMcdModifyPrice


@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    logging.debug("====> saludo:{}".format(nombre))
    return {"Te saludo "+nombre+" primero con tu nombre."}

#APIS que utilizan las funciones de Utils
@app.get("/sumar/")
def apiSuma(num1: int, num2: int):
    return {"La suma es " + str(Suma(num1, num2)) + "."}

@app.get("/restar/")
def apiResta(num1: int, num2: int):
    return {"La resta es " + str(Resta(num1, num2)) + "."}