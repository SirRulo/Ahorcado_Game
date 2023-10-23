import pygame

def generar_fuente(escritura:str, tamaño:int):
    return pygame.font.SysFont(escritura,tamaño)

def mostrar_texto(fuente, pantalla, palabra:str, color, x, y):
    try:
        texto = fuente.render(palabra, True, color)
        pantalla.blit(texto,(x,y))
    except Exception as error:
        print(f"ERROR! -> {error}")