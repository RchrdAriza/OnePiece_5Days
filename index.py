import pygame

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



class Luffy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # self.image = pygame.image.load('recursos/imagenes/quieto.png').convert()
        self.image = pygame.transform.scale(pygame.image.load('recursos/imagenes/quieto.png').convert(), (150, 150))
        self.rect = self.image.get_rect()

        self.rect.center = (ANCHO // 2, ALTO // 2)

    def update(self):

        teclas = pygame.key.get_pressed()







pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('One piece')
clock = pygame.time.Clock()

# Sprites

luffy = pygame.sprite.Group()

jugador = Luffy()
luffy.add(jugador)

ejecutando = True
while ejecutando:

    clock.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    luffy.update()

    luffy.draw(pantalla)
    pygame.display.flip()

pygame.quit
