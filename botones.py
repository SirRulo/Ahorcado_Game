from imagen import *

# Medidas Botones
ancho_boton = 250
alto_boton = 100

# Coordenadas
play_x = 100
score_x = 465
exit_x = 850
reset_x = 300
menu_x = 650
buttons_y = 600

def generar_superficie(ancho, alto):
    return pygame.Surface((ancho, alto))

def convertir_boton(archivo_imagen:str, ancho, alto):
    boton = generar_superficie(ancho,alto)
    boton = escalar_imagen(archivo_imagen, ancho, alto)
    return boton

play = convertir_boton("Ahorcado\\Imagenes\\play.png", ancho_boton,alto_boton)
exit = convertir_boton("Ahorcado\\Imagenes\\exit.png", ancho_boton,alto_boton)
score = convertir_boton("Ahorcado\\Imagenes\\score.png", ancho_boton,alto_boton)
reset = convertir_boton("Ahorcado\\Imagenes\\reset.png", ancho_boton,alto_boton)
menu = convertir_boton("Ahorcado\\Imagenes\\menu.jpg", ancho_boton,alto_boton)