import pygame

def cargar_imagen(archivo_imagen:str):
    # brief: carga la imagen pasandole como parametro el path de la imagen.
    # parametros:
    #     archivo_imagen: string que define el relative path de la imagen.
    # return: carga de una imagen
    return pygame.image.load(archivo_imagen)

def escalar_imagen(archivo_imagen:str, largo, ancho):
    # brief: escala la imagen con las medidas que quieras y pasandole el path del mismo.
    # parametros:
    #     archivo_imagen: string que define el relative path de la imagen.
    #     largo: medida del largo para escalar la imagen.
    #     ancho: medida del ancho para escalar la imagen.
    # return: imagen escalada
    imagen = cargar_imagen(archivo_imagen)
    imagen = pygame.transform.scale(imagen,(largo,ancho))
    return imagen

def setear_icono(archivo_imagen:str):
    # brief: setea una imagen para comvertirlo en icono del programa.
    # parametros:
    #     archivo_imagen: string que define el relative path de la imagen.
    # return: imagen seteada a icono del programa
    imagen = cargar_imagen(archivo_imagen)
    return pygame.display.set_icon(imagen)