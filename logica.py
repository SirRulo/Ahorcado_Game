from visual import *
from archivo_json_csv import *
import sys
import random

def ahorcado_game():
    # brief: la funcion principal del juego; aqui es donde se resuelve toda la logica; contiene sus variables y llamadas a funciones para su completo funcionamiento.
    # parametros: -
    # return: -
    lista_palabras = leer_palabras_json("Ahorcado/Archivos/palabras.json")

    # Variables
    puntaje = 0
    adivinadas = 0
    usuario = []
    game_over = False
    play_game = False
    score_view = False
    score_flag = False
    you_win = False

    # Configura el timer
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    tiempo_transcurrido = 0

    # Loop principal
    run = True
    while run == True:
        lista_eventos = pygame.event.get()
        if play_game == False and score_view == False:
            PANTALLA.fill(NEGRO)
            PANTALLA.blit(titulo,(425,100))
            PANTALLA.blit(play,(play_x,buttons_y))
            PANTALLA.blit(score,(score_x,buttons_y))
            PANTALLA.blit(exit,(exit_x,buttons_y))
            palabra_adivinada = True
        elif score_view == True:
            if score_flag == False:
                lista_scores = []
                y = 120

                PANTALLA.fill(NEGRO)
                dibujar_rectangulo(PANTALLA, VERDE, 350,100,500,700,5)
                mostrar_texto(fuente_3, PANTALLA, "NAMES", BLANCO, 410,50)
                mostrar_texto(fuente_3, PANTALLA, "SCORES", BLANCO, 690,50)
                mostrar_texto(fuente_3, PANTALLA, "press ENTER to continue...", BLANCO, 400,820)

                lista_scores = leer_score_csv("Ahorcado/Archivos/scores.csv", lista_scores)
                for elemento in lista_scores:
                    nombre = elemento["nombre"]
                    punto = elemento["punto"]

                    mostrar_texto(fuente_2, PANTALLA, nombre, BLANCO, 400,y)
                    mostrar_texto(fuente_2, PANTALLA, punto, BLANCO, 700,y)

                    y += 50
                score_flag = True
        elif you_win == True:
            PANTALLA.fill(NEGRO)
            PANTALLA.blit(win,(350,100))
            PANTALLA.blit(star,(530,650))

            dibujar_rectangulo(PANTALLA, VERDE, 480,480,220,100,5)
            mostrar_texto(fuente_3, PANTALLA, "Name...? (5 max)", BLANCO, 480,430)
            mostrar_texto(fuente_3, PANTALLA, str(puntaje), BLANCO, 600,650)

            usuario = "".join(usuario)
            mostrar_texto(fuente, PANTALLA, usuario, BLANCO, 500,500)
        elif palabra_adivinada == True and play_game == True:
            PANTALLA.fill(NEGRO)
            tematica_elegida = random.choice(lista_palabras)
            palabra_elegida = random.choice(tematica_elegida["palabras"])
            
            palabra_oculta = re.sub("[A-Z]", "_ ", palabra_elegida)
            palabra_oculta = re.split(" ", palabra_oculta)
            palabra_oculta.remove("")
            
            # Re/Iniciar el timer
            tiempo_inicial = 60
            tiempo_transcurrido = tiempo_inicial

            PANTALLA.blit(timer,(40,50))
            PANTALLA.blit(star,(40,110))
            PANTALLA.blit(tick,(1000,50))
            PANTALLA.blit(book,(430,390))

            mostrar_texto(fuente_3, PANTALLA, tematica_elegida["tema"], BLANCO, 530,400)
            mostrar_texto(fuente_3, PANTALLA, f"{adivinadas}/10", BLANCO, 1050,50)
            mostrar_texto(fuente_2, PANTALLA, f"{puntaje}", BLANCO, 100,110)
            mostrar_texto(fuente_2, PANTALLA, " ".join(palabra_oculta), BLANCO, 380,500)

            letras_ingresadas = []
            intentos = 9
            palabra_adivinada = False
        elif "_" not in palabra_oculta:
            puntaje = puntaje + tiempo_transcurrido
            adivinadas += 1

            if adivinadas == 10:
                palabra_oculta = "_"
                adivinadas = 0
                you_win = True
            else:
                palabra_adivinada = True
        elif game_over == True:
            PANTALLA.fill(NEGRO)
            PANTALLA.blit(over,(350,100))
            PANTALLA.blit(reset,(reset_x,buttons_y))
            PANTALLA.blit(menu,(menu_x,buttons_y))
            adivinadas = 0

        try:
            for evento in lista_eventos:
                if evento.type == pygame.USEREVENT and (play_game == True and game_over == False and you_win == False):
                    dibujar_rectangulo(PANTALLA, NEGRO, 90,50,50,40)
                    mostrar_texto(fuente_2, PANTALLA, f"{tiempo_transcurrido}", BLANCO, 90,50)
                    
                    if tiempo_transcurrido == 0:
                        game_over = True
                    else:
                        tiempo_transcurrido -= 1

                if evento.type == pygame.QUIT:
                    run = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1  and play_game == False:
                        if play_x < evento.pos[0] < play_x + ancho_boton and buttons_y < evento.pos[1] < buttons_y + alto_boton:
                            play_game = True
                        elif score_x < evento.pos[0] < score_x + ancho_boton and buttons_y < evento.pos[1] < buttons_y + alto_boton:
                            score_view = True
                        elif exit_x < evento.pos[0] < exit_x + ancho_boton and buttons_y < evento.pos[1] < buttons_y + alto_boton:
                            run = False
                    elif evento.button == 1 and game_over == True:
                        if reset_x < evento.pos[0] < reset_x + ancho_boton and buttons_y < evento.pos[1] < buttons_y + alto_boton:
                            game_over = False
                            palabra_adivinada = True
                            puntaje = 0
                        elif menu_x < evento.pos[0] < menu_x + ancho_boton and buttons_y < evento.pos[1] < buttons_y + alto_boton:
                            game_over = False
                            play_game = False
                            palabra_adivinada = True
                            puntaje = 0
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN and score_view == True:
                        score_view = False
                        score_flag = False
                    elif(evento.key >= pygame.K_a and evento.key <= pygame.K_z) and you_win == True:
                        letra = chr(evento.key).upper()

                        usuario = list(usuario)
                        usuario.append(letra)
                        if len(usuario) == 5:
                            nuevo_usuario = []
                            usuario = "".join(usuario)
                            nuevo_usuario.append(usuario)
                            nuevo_usuario.append(str(puntaje))
                            nuevo_usuario = ",".join(nuevo_usuario)

                            agregar_usuario_csv("Ahorcado/Archivos/scores.csv", nuevo_usuario)

                            usuario = []
                            puntaje = 0
                            you_win = False
                            play_game = False
                    elif (evento.key >= pygame.K_a and evento.key <= pygame.K_z) and (game_over == False and play_game == True and you_win == False):
                        bandera = False
                        letra = chr(evento.key).upper()

                        letras_ingresadas = list(letras_ingresadas)
                        if letra in letras_ingresadas:
                            bandera = -1
                        else:
                            for i in range(len(palabra_elegida)):
                                if palabra_elegida[i] == letra:
                                    palabra_oculta[i] = letra
                                    bandera = True

                        if bandera == True:
                            puntaje += 10
                        elif bandera == False:
                            intentos -= 1
                            if puntaje == 0:
                                pass
                            else:
                                puntaje -= 5
                            
                            if intentos > 0:
                                dibujar_figura(intentos)
                            else:
                                game_over = True

                        letras_ingresadas.append(letra)
                        letras_ingresadas = set(letras_ingresadas)

                        dibujar_rectangulo(PANTALLA, NEGRO, 380,500,800,100)
                        dibujar_rectangulo(PANTALLA, NEGRO, 100,110,150,40)

                        mostrar_texto(fuente_2, PANTALLA, f"{puntaje}", BLANCO, 100,110)
                        mostrar_texto(fuente, PANTALLA, " ".join(palabra_oculta), BLANCO, 380,500)
        except Exception as error:
            print(f"ERROR! -> {error}")
        pygame.display.flip()
    pygame.quit()
    sys.exit()