import pygame

def generar_fuente(escritura:str, tamaño:int):
    # brief: genera una fuente para un texto.
    # parametros:
    #     escritura: el tipo de fuente que quieras implementar en el texto.
    #     tamaño: el tamaño del texto.
    # return: fuente de texto
    return pygame.font.SysFont(escritura,tamaño)

def mostrar_texto(fuente, pantalla, palabra:str, color, x, y):
    # brief: muestra el texto en pantalla de pygame.
    # parametros:
    #     fuente: la fuente del texto.
    #     pantalla: las medidas de la pantalla del programa.
    #     palabra: el texto que quieras mostrar en pantalla.
    #     color: el color del texto.
    #     x: la coordenada "x" de la pantalla donde se mostrara el texto en pantalla.
    #     y: la coordenada "y" de la pantalla donde se mostrara el texto en pantalla.
    # return: -
    try:
        texto = fuente.render(palabra, True, color)
        pantalla.blit(texto,(x,y))
    except Exception as error:
        print(f"ERROR! -> {error}")