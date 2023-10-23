import pygame

def cargar_imagen(archivo_imagen:str):
    return pygame.image.load(archivo_imagen)

def escalar_imagen(archivo_imagen:str, largo, ancho):
    imagen = cargar_imagen(archivo_imagen)
    imagen = pygame.transform.scale(imagen,(largo,ancho))
    return imagen

def setear_icono(archivo_imagen:str):
    imagen = cargar_imagen(archivo_imagen)
    return pygame.display.set_icon(imagen)