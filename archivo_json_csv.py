import json
import re

def leer_palabras_json(archivo_json:str):
    # brief: permite leer el archivo de tipo "JSON" con las palabras y tematicas que hay en ella para luego volverlo una lista.
    # parametros:
    #     archivo_json: el path del archivo JSON.
    # return: lista del archivo JSON
    try:
        with open(archivo_json, "r") as archivo:
            palabras = json.load(archivo)
        lista = palabras["palabras"]
    except Exception as error:
        print(f"ERROR! -> {error}")
    return lista

def leer_score_csv(archivo_csv:str, lista:list):
    # brief: permite leer el archivo de tipo "CSV" con los puntajes de cada usuario que hay en ella para luego volverlo una lista.
    # parametros:
    #     archivo_csv: el path del archivo CSV.
    # return: lista del archivo CSV
    with open(archivo_csv, "r") as archivo:
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
    # brief: permite sobreescribir el archivo de tipo "CSV" agregando un nuevo usuario con su puntaje al ganar el juego.
    # parametros:
    #     archivo_csv: el path del archivo CSV.
    #     player: el nombre del usuario con su puntaje.
    # return: -
    with open(archivo_csv, "a") as archivo:
        archivo.write(f"\n{player}")