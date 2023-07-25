import pygame
# import sys
# sys.path.append("..")
from ..personajes.luffy import Jugador

FONDO_ANCHO = 2738
FONDO_ALTO = 600

ANCHO = 800
ALTO = 600

FPS = 30

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
H_FA2F2F = (255, 47, 47)
VERDE = (0, 255, 0)
AZUL = (0,0, 255)
AZUL2 = (64, 64, 255)
H_50D2FE = (94, 210, 254)

background_x = 0


class Alvidalevel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    # self.pantalla1 = pygame.display.set_mode((ANCHO, ALTO))
    # pygame.display.set_caption('Level: 01')

    def update(self):
        global background_x
        # jugador.rect.x += 10
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            background_x += 10
            jugador.correr_derecha()
            

        if key[pygame.K_a]:
            background_x -= 10
            jugador.correr_izquierda()

        
        if background_x > 0:
            background_x = 0

        # Limite derecho del fondo (no se desplaza más allá del borde derecho de la imagen de fondo)
        limite_derecho = FONDO_ANCHO - ANCHO
        if background_x < -limite_derecho:
            background_x = -limite_derecho

if __name__ == "__main__":

    pygame.init()
    pantalla1 = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Level: 01')
    imagen_fondo = pygame.image.load('../recursos/imagenes/alvidabarcodentro.jpg')
    nivel1 = Alvidalevel()
    jugador = Jugador()
    luffy = pygame.sprite.Group()
    luffy.add(jugador)
    while nivel1:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                nivel1 = False
        pantalla1.blit(imagen_fondo, (background_x, 0))
        luffy.draw(pantalla1)
        luffy.update()
        pygame.display.flip()

    pygame.quit


