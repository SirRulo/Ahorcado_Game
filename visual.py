from figuras import *
from botones import *
from texto import *

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO,LARGO = 1200,900
PANTALLA = pygame.display.set_mode((ANCHO,LARGO))
pygame.display.set_caption("AHORCADO")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0,255,0)

def dibujar_figura(cant_intentos):
    # brief: dibuja el muñequito del ahorcado al ir perdiendo intentos o errando en la letra que vaya ingresando el usuario.
    # parametros:
    #     cant_intentos: numero de intentos que ira decresiendo al ingresar mal una letra.
    # return: -
    match(cant_intentos):
        case 8:
            dibujar_linea(PANTALLA, VERDE, 500,300, 530,300,5)
            dibujar_linea(PANTALLA, VERDE, 515,50, 515,300,5)
        case 7:
            dibujar_linea(PANTALLA, VERDE, 515,50, 620,50,5)
            dibujar_linea(PANTALLA, VERDE, 620,50, 620,70,5)
        case 6:
            dibujar_circulo(PANTALLA, VERDE, 620,100, 30,5)
        case 5:
            dibujar_linea(PANTALLA, VERDE, 620,130, 620,200,5)
        case 4:
            dibujar_linea(PANTALLA, VERDE, 620,140, 670,170,5)
        case 3:
            dibujar_linea(PANTALLA, VERDE, 620,140, 570,170,5)
        case 2:
            dibujar_linea(PANTALLA, VERDE, 620,200, 570,270,5)
        case 1:
            dibujar_linea(PANTALLA, VERDE, 620,200, 670,270,5)


# Fuentes Texto
fuente = generar_fuente("Times New Roman",60)
fuente_2 = generar_fuente("Console",45)
fuente_3 = generar_fuente("Impact",40)

# Imagenes
icono = setear_icono("Ahorcado\\Imagenes\\ahorcado.jpg")
titulo = cargar_imagen("Ahorcado\\Imagenes\\titulo.jpg")
timer = escalar_imagen("Ahorcado\\Imagenes\\timer.png",50,50)
star = escalar_imagen("Ahorcado\\Imagenes\\star.png",50,50)
book = escalar_imagen("Ahorcado\\Imagenes\\book.png",70,70)
tick = escalar_imagen("Ahorcado\\Imagenes\\tick.png",50,50)
win = escalar_imagen("Ahorcado\\Imagenes\\win.jpg",500,300)
over = escalar_imagen("Ahorcado\\Imagenes\\game over.png",500,300)