import pygame
import personajes
import sys

pygame.init()

# Medidas de la pantalla
width = 800
height = 600
fps =  60
ventana = pygame.display.set_mode((width, height))
pygame.display.set_caption("Atrapados")
velocidad = 3

# Esta funcion es la que crea el menu donde comienza el juego
def draw_menu(ventana):
    menu_font = pygame.font.Font(None, 36)
    start_button_font = pygame.font.Font(None, 24)
    start_button_rect = pygame.Rect(width // 2 - 50, height // 2, 100, 50)
    start_text = start_button_font.render("Start", True, (0, 255, 255))
    start_text_rect = start_text.get_rect(center=start_button_rect.center)

    ventana.fill((0, 0, 0))
    menu_text = menu_font.render("Bienvenido a Atrapados", True, (255, 255, 255))
    ventana.blit(menu_text, (width // 2 - menu_text.get_width() // 2, height // 2 - 100))
    pygame.draw.rect(ventana, (0, 0, 0), start_button_rect)
    ventana.blit(start_text, start_text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                game_loop()

def game_over():
    menu_font = pygame.font.Font(None, 36)
    start_button_font = pygame.font.Font(None, 24)
    start_button_rect = pygame.Rect(width // 2 - 50, height // 2, 100, 50)
    start_text = start_button_font.render("Reiniciar", True, (0, 255, 255))
    start_text_rect = start_text.get_rect(center=start_button_rect.center)

    ventana.fill((0, 0, 0))
    menu_text = menu_font.render("Has Perdido!", True, (255, 255, 255))
    ventana.blit(menu_text, (width // 2 - menu_text.get_width() // 2, height // 2 - 100))
    pygame.draw.rect(ventana, (0, 0, 0), start_button_rect)
    ventana.blit(start_text, start_text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                # Reset the game
                game_loop()

def ganador():
    menu_font = pygame.font.Font(None, 36)
    start_button_font = pygame.font.Font(None, 24)
    start_button_rect = pygame.Rect(width // 2 - 50, height // 2, 100, 50)
    start_text = start_button_font.render("Volver a jugar", True, (0, 255, 255))
    start_text_rect = start_text.get_rect(center=start_button_rect.center)
    
    ventana.fill((0, 0, 0))
    menu_text = menu_font.render("Has Ganado!", True, (255, 255, 255))
    ventana.blit(menu_text, (width // 2 - menu_text.get_width() // 2, height // 2 - 100))
    pygame.draw.rect(ventana, (0, 0, 0), start_button_rect)
    ventana.blit(start_text, start_text_rect)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # Con esta condición si el jugador oprime la X se cierra el programa 
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos): # O si oprime el boton, se ejecuta el loop principal del juego
                # Reset the game
                game_loop()


# Este es el loop principal donde se desenvuelve todo el juego
def game_loop():
    # Esta funcion crea la imagen
    def crear_img(image, scale):
        ancho = image.get_width()
        alto = image.get_height()
        nuevo = pygame.transform.scale(image, (ancho*scale, alto*scale))
        return nuevo

    # Aqui se guardan las imagenes del protagonista y el enemigo para crear la animación
    animacion_protagonista = []
    for i in range(6):
        img = pygame.image.load(f"media//protagonista//mov{i+1}.png")
        img = crear_img(img, 2)
        animacion_protagonista.append(img)
    animacion_enemigo = []
    for i in range(4):
        img = pygame.image.load(f"media//enemigo//mov{i}.png")
        img = crear_img(img, 2)
        animacion_enemigo.append(img)

    # Construccion y ubicación de objetos
    enemigo1 = personajes.Enemigo(400, 450, animacion_enemigo, 2)
    enemigo2 = personajes.Enemigo(300, 240, animacion_enemigo, 2)
    enemigo3 = personajes.Enemigo(600, 300, animacion_enemigo, 2)
    enemigo4 = personajes.Enemigo(700, 100, animacion_enemigo, 2)
    protagonista = personajes.Personaje(50, 50, animacion_protagonista) # Se crea (construye) el jugador y se orienda en las coordenadas 50, 50
    puerta = personajes.Puerta(740,530, pygame.image.load("media/puerta.png"))

    # Definicion de variables de movimiento
    arriba = False
    abajo = False
    izquierda = False
    derecha = False
    vidas = 3 # Numero de vidas del jugador

    reloj = pygame.time.Clock() # Controla los FPS
    run  = True # Será nuestra variable para el loop principal del juego

    vidas_font = pygame.font.Font(None, 36) # Se define el tipo de fuente para el texto de "vidas"

    while run:
        reloj.tick(60)
        ventana.fill((0,0,20))

        # Movimiento del jugador y enemigo
        Px, Py = 0, 0 # Px -> moviemiento en X y Y del protagonista
        if derecha == True:
            Px = velocidad
        if izquierda == True:
            Px = -velocidad
        if arriba == True:
            Py = -velocidad
        if abajo == True:
            Py = velocidad

        # Mover el jugador
        protagonista.movimiento(Px,Py, width, height)
        protagonista.update()
        protagonista.dibujar(ventana) # Aquí dibuja al jugador en la ventana
    
        # Mover a los enemigos 
        enemigo1.update()
        enemigo1.dibujar(ventana)
        enemigo2.update()
        enemigo2.dibujar(ventana)
        enemigo3.update()
        enemigo3.dibujar(ventana)
        enemigo4.update()
        enemigo4.dibujar(ventana)
    
        # Aquí se dibuja la puerta
        puerta.dibujar(ventana)

        # Se comprueba si choca con los enemigos
        if personajes.colision(protagonista, enemigo1) or personajes.colision(protagonista, enemigo2) or personajes.colision(protagonista, enemigo3) or personajes.colision(protagonista, enemigo4):
            vidas -= 1
            protagonista.forma.center = (50, 50)
        elif personajes.colision(protagonista, puerta): # Cuando llega a la puerta, gana
            ganador()
        
        if vidas < 1: # Si ya no tiene vidas, pierde
            game_over()

        # Este es el render del texto del juego que dice "vidas"
        vidas_label = vidas_font.render(f"Vidas: {vidas}", True, (255, 255, 255))
        vidas_rect = vidas_label.get_rect(topleft=(10, 10))
        ventana.blit(vidas_label, vidas_rect)

        for event in pygame.event.get(): # Revisa los eventos que se hagan dentro del juego
            if event.type == pygame.QUIT: # Cerrar la ventana desde la X de la esquina superior derecha
                run = False # Asi el While no corre y se cierra la ventana
            if event.type == pygame.KEYDOWN: # Con esta condicional el programa reconoce las teclas ASDW para el movimiento arriba, abajo y a los lados
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    izquierda = True
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    derecha = True
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    abajo = True
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    arriba = True
            
            if event.type == pygame.KEYUP: # Si no se tiene oprimida la tecla, no se debe mover el personaje
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    izquierda = False
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    derecha = False
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    abajo = False
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    arriba = False
        pygame.display.update() # Con esta linea de código, el programa se va actualizando continuamente

#aquí se inicializa el juego
def main():
    while True:
        draw_menu(ventana)
        pygame.display.flip()

if __name__ == '__main__':
    main()