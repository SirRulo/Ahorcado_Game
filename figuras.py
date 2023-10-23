import pygame

def dibujar_linea(pantalla, color, x_i, y_i, x_f, y_f, grosor=0):
    pygame.draw.line(pantalla, color, (x_i,y_i),(x_f,y_f),grosor)

def dibujar_circulo(pantalla, color, x, y, radio, grosor=0):
    pygame.draw.circle(pantalla, color, (x, y), radio,grosor)

def dibujar_rectangulo(pantalla, color, x, y, ancho, alto, grosor=0):
    pygame.draw.rect(pantalla, color, (x, y, ancho, alto),grosor)