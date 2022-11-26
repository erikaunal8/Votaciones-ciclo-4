from pymongo import MongoClient
import json
import certifi

ca = certifi.where()

##############################################
# funcion cargar el archivo de configuracion #
###############################################
def loadConfigFile():
    with open('database/config.json') as f:
        data = json.load(f)
    return data 

###################################
#  funcion de conexion       #
##################################
def dbconnection():
    dataConfig = loadConfigFile()
    try:
        #conexion atlas
        client = MongoClient(dataConfig['MONGO_URI_SERVER'],  tlsCAFile =  ca
        #conexion local
        client = MongoClient(dataConfig['MONGO_URI_LOCAL'], dataConfig['LOCAL_PORT'])
        db = client["ciclo4_votaciones_domingo"]
     except: ConnectionError:
        print("Error de conexion con la db") 
    return db     