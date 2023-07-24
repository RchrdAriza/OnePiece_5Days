import pygame
import time
ANCHO = 800
ALTO = 600

FONDO_ANCHO = 2738
FONDO_ALTO = 600

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

class Luffy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # self.image = pygame.image.load('recursos/imagenes/quieto.png').convert()
        self.image = pygame.transform.scale(pygame.image.load('recursos/imagenes/quieto.png').convert(), (150, 150))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()

        self.rect.center = (200, 370)

        # self.CONTADOR = 0
        self.tiempo_inicial = time.time()

        # posicion inicial
        self.velocidad_x = 0
        self.velocidad_y = 0

        self.imagenes_movimiento = [
                'recursos/imagenes/Run1.png',
                'recursos/imagenes/Run2.png',
                'recursos/imagenes/Run3.png',
                'recursos/imagenes/Run4.png',
                'recursos/imagenes/Run5.png',
                'recursos/imagenes/Run6.png',
                'recursos/imagenes/Run7.png',
                'recursos/imagenes/Run8.png'
                ]
        self.indice_imagen_actual = 0
        self.imagen_correr = pygame.image.load(self.imagenes_movimiento[self.indice_imagen_actual]).convert()
    
    def correr(self):
        self.velocidad_x = 5
        self.indice_imagen_actual += 1
        if self.indice_imagen_actual >= len(self.imagenes_movimiento):
            self.indice_imagen_actual = 0
        self.image_correr = pygame.transform.scale(pygame.image.load(self.imagenes_movimiento[self.indice_imagen_actual]).convert_alpha(), (150, 150))
        self.image.set_colorkey(NEGRO)

    def update(self):

        global background_x

        self.velocidad_x = 0
        self.velocidad_y = 0
        teclas = pygame.key.get_pressed()

        tiempo_transcurrido = time.time() - self.tiempo_inicial

        if teclas[pygame.K_d]:
            # self.velocidad_x += 10
            self.correr()
            background_x -= 10 
        
        if teclas[pygame.K_a]:
            self.velocidad_x -= 10
            background_x += 10

        self.rect.x += self.velocidad_x
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > ANCHO:
            self.rect.right = ANCHO

        # Limite izquierdo del fondo (no se desplaza más allá del borde izquierdo de la ventana)
        if background_x > 0:
            background_x = 0

        # Limite derecho del fondo (no se desplaza más allá del borde derecho de la imagen de fondo)
        limite_derecho = FONDO_ANCHO - ANCHO
        if background_x < -limite_derecho:
            background_x = -limite_derecho

class Escalon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load('recursos/spritescolisiones/escalon.jpg').convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        # self.rect.center = (700, 400)
        self.rect.x = x
        self.rect.y = y









pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('One piece')
clock = pygame.time.Clock()
# Sprites

luffy = pygame.sprite.Group()
piso = pygame.sprite.Group()

jugador = Luffy()
luffy.add(jugador)

escalon = Escalon(700, 400)
piso.add(escalon)

ejecutando = True
while ejecutando:

    clock.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # cargar fondo
    fondo = pygame.image.load('recursos/imagenes/alvidabarcodentro.jpg')
    pantalla.blit(fondo, (background_x, 0))

    piso.update()
    piso.draw(pantalla)
    luffy.update()
    luffy.draw(pantalla)
    pygame.display.flip()

pygame.quit
