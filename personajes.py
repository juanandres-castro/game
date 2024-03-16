import pygame

class Personaje:
    def __init__(self, x, y, animacion):
        self.flip = False
        self.animaciones = animacion
        self.frame = 0
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.image = self.animaciones[self.frame]
        self.forma = pygame.Rect(0, 0, 20, 20)  # Crea el personaje en las coordenadas 0,0 con dimensiones 20x20
        self.forma.center = (self.x, self.y)  # Coloca el personaje en las coordenadas X, Y
        self.update_time = pygame.time.get_ticks()

    def update(self):
        tiempo = 80
        self.image = self.animaciones[self.frame]
        if pygame.time.get_ticks() - self.update_time >= tiempo:
            self.frame += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame >= len(self.animaciones):
            self.frame = 0

    def dibujar(self, ventana):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        ventana.blit(imagen_flip, self.forma)

    def movimiento(self, Dx, Dy, ventana_ancho, ventana_alto):
        if Dx < 0:
            self.flip = True
        if Dx > 0:
            self.flip = False

        # Actualiza la posición del personaje
        self.forma.x = max(0, min(self.forma.x + Dx, ventana_ancho - self.forma.width))
        self.forma.y = max(0, min(self.forma.y + Dy, ventana_alto - self.forma.height))

class Enemigo():

    def __init__(self, x, y, animaciones, vel):
        self.flip = False
        self.animaciones = animaciones
        self.frame = 0
        self.width = 80
        self.height = 15
        self.image = self.animaciones[self.frame]
        self.forma = pygame.Rect(0, 0, self.width, self.height)  # Se crea el personaje en las coordenadas 0,0 con las dimensiones 20, 20
        self.x = x
        self.y = y
        self.update_time = pygame.time.get_ticks()
        self.velocidad = vel
        self.direction = 1


    def update(self):
        tiempo = 80
        self.image = self.animaciones[self.frame]
        if pygame.time.get_ticks() - self.update_time >= tiempo:
            self.frame += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame >= len(self.animaciones):
            self.frame = 0
        self.x += self.velocidad * self.direction
        if self.x < 0 or self.x + self.width > 800:
            self.direction *= -1

    def dibujar(self, ventana):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        ventana.blit(imagen_flip, (self.x, self.y))

class Puerta():
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.image = img
    
    def dibujar(self, ventana):
        img_final = pygame.transform.scale(self.image, (self.width, self.height))
        ventana.blit(img_final, (self.x, self.y))

def colision(protagonista, enemigo):
    if protagonista.forma.x < enemigo.x + enemigo.width and protagonista.forma.x + protagonista.width > enemigo.x and protagonista.forma.y < enemigo.y + enemigo.height and protagonista.forma.y + protagonista.height > enemigo.y:
        return True
    else:
        return False