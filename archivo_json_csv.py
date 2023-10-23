import json
import re

def leer_palabras_json(archivo_json:str):
    try:
        with open(archivo_json, "r") as archivo:
            palabras = json.load(archivo)
        lista = palabras["palabras"]
    except Exception as error:
        print(f"ERROR! -> {error}")
    return lista

def leer_score_csv(archivo_csv:str, lista:list):
    with open("Ahorcado/Archivos/scores.csv", "r") as archivo:
        try:
            for linea in archivo:
                linea = re.split(r",|\n", linea)
                u_score = {}
                u_score["nombre"] = linea[0]
                u_score["punto"] = linea[1]
                lista.append(u_score)
        except Exception as error:
            print(f"ERROR! -> {error}")
    return lista

def agregar_usuario_csv(archivo_csv:str, player):
    with open("Ahorcado/Archivos/scores.csv", "a") as archivo:
        archivo.write(f"\n{player}")