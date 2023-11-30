import pygame

def dibujar_linea(pantalla, color, x_i, y_i, x_f, y_f, grosor=0):
    # brief: dibuja una linea en la pantalla de pygame.
    # parametros:
    #     pantalla: las medidas de la pantalla del programa.
    #     color: el color de la linea a dibujar.
    #     x_i: la coordenada "x" que define el punto en donde inicia el dibujo de la linea.
    #     y_i: la coordenada "y" que define el punto en donde inicia el dibujo de la linea.
    #     x_f: la coordenada "x" que define el punto en donde finaliza el dibujo de la linea.
    #     y_f: la coordenada "y" que define el punto en donde finaliza el dibujo de la linea.
    #     grosor: (opcional) define el grosor de la linea.
    # return: -
    pygame.draw.line(pantalla, color, (x_i,y_i),(x_f,y_f),grosor)

def dibujar_circulo(pantalla, color, x, y, radio, grosor=0):
    # brief: dibuja un circulo en la pantalla de pygame.
    # parametros:
    #     pantalla: las medidas de la pantalla del programa.
    #     color: el color del circulo a dibujar.
    #     x: la coordenada "x" que define el punto en donde se dibuja el circulo.
    #     y: la coordenada "y" que define el punto en donde se dibuja el circulo.
    #     radio: medida del circulo.
    #     grosor: (opcional) define el grosor del circulo.
    # return: -
    pygame.draw.circle(pantalla, color, (x, y), radio,grosor)

def dibujar_rectangulo(pantalla, color, x, y, ancho, alto, grosor=0):
    # brief: dibuja un rectangulo en la pantalla de pygame.
    # parametros:
    #     pantalla: las medidas de la pantalla del programa.
    #     color: el color del rectangulo a dibujar.
    #     x: la coordenada "x" que define el punto en donde se dibuja el rectangulo.
    #     y: la coordenada "y" que define el punto en donde se dibuja el rectangulo.
    #     ancho: medida del ancho del rectangulo.
    #     alto: medida del alto del rectangulo.
    #     grosor: (opcional) define el grosor del rectangulo.
    # return: -
    pygame.draw.rect(pantalla, color, (x, y, ancho, alto),grosor)