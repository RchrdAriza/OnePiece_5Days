import pygame, time, os
from pygame.locals import *
from 
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

BACKGROUND_X = 0

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    

        # Obtener la ruta del archivo actual
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        print(directorio_actual)
        # Construir la ruta a la imagen relativa al archivo actual
        ruta_imagen = os.path.join(directorio_actual, '..', 'recursos', 'imagenes', '{}')

        # Cargar la imagen y redimensionarla
        self.image = pygame.transform.scale(pygame.image.load(ruta_imagen.format("quieto.png")).convert(), (90, 110))


        # self.image = pygame.transform.scale(pygame.image.load('recursos/imagenes/quieto.png').convert(), (90, 110))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.center = (200, 500)
        self.posicion_x = 0
        ruta_imagen_correr = os.path.join(directorio_actual, '..', 'recursos', 'imagenes', '{}')

        self.correr_lista = [pygame.image.load(ruta_imagen_correr.format("Run1.png")),
                             pygame.image.load(ruta_imagen_correr.format("Run2.png")),
                             pygame.image.load(ruta_imagen_correr.format("Run3.png")),
                             pygame.image.load(ruta_imagen_correr.format("Run4.png")),
                             pygame.image.load(ruta_imagen_correr.format("Run5.png")),
                             pygame.image.load(ruta_imagen_correr.format("Run6.png")),
                             pygame.image.load(ruta_imagen_correr.format("Run7.png")),
                             pygame.image.load(ruta_imagen_correr.format("Run8.png")),]
        # quedarse dormido

        # self.demasiado_quieto_secuencia = [pygame.image.load('recursos/imagenes/Demasiadoquieto1.png'),
        #                                 pygame.image.load('recursos/imagenes/Demasiadoquieto2.png'),
        #                                 pygame.image.load('recursos/imagenes/Demasiadoquieto3.png'),
        #                                 pygame.image.load('recursos/imagenes/Demasiadoquieto4.png'),
        #                                 pygame.image.load('recursos/imagenes/Demasiadoquieto5.png'),]
        #
        self.indice_correr = 0
        # self.indice_demasiado_quieto = 0
        # self.velocidad_secuencia_demasiado_quieto = 5
        self.velocidad_correr = 8
        self.movimiento_derecha = False
        self.movimiento_izquierda = False
        self.tiempo_inicial = time.time()

    def update(self):

        # self.posicion_x = 0

        tiempo_transcurrido = time.time() - self.tiempo_inicial
        global BACKGROUND_X

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_d]:
            self.indice_correr += 1
            if self.indice_correr == len(self.correr_lista) * self.velocidad_correr:
                self.indice_correr = 0
            imagen_actual = self.correr_lista[self.indice_correr // self.velocidad_correr]

            # Actualizar la imagen del jugador
            self.image = pygame.transform.scale(imagen_actual, (90, 110))
            self.image.set_colorkey(NEGRO)
            # self.posicion_x += 10
            self.rect.x += 10
            self.movimiento_derecha = True

        else:
            self.movimiento_derecha = False
        
        if teclas[pygame.K_a]:
            # self.posicion_x -= 10
            if self.indice_correr == len(self.correr_lista) * self.velocidad_correr:
                self.indice_correr = 0
            imagen_actual = self.correr_lista[self.indice_correr // self.velocidad_correr]
            imagen_volteada_horizontalmente = pygame.transform.flip(imagen_actual, True, False)


            # Actualizar la imagen del jugador
            self.image = pygame.transform.scale(imagen_volteada_horizontalmente, (90, 110))
            self.image.set_colorkey(NEGRO)
            # self.posicion_x += 10
            self.rect.x -= 10
            self.movimiento_izquierda = True
            self.indice_correr += 1

        else:
            # self.posicion_x = 0
            self.movimiento_izquierda = False

        if not self.movimiento_derecha and not self.movimiento_izquierda:
            quieto_img = pygame.transform.scale(pygame.image.load('recursos/imagenes/quieto.png').convert(), (90, 130))
            quieto_img.set_colorkey(NEGRO)
            self.image = quieto_img
            # if tiempo_transcurrido > 5:
                # if self.indice_demasiado_quieto == len(self.demasiado_quieto_secuencia) * self.velocidad_secuencia_demasiado_quieto:
                #     self.indice_demasiado_quieto = 0
                # imagen_demasiado_quieto = self.demasiado_quieto_secuencia[self.indice_demasiado_quieto // self.velocidad_secuencia_demasiado_quieto]
                # self.image = pygame.transform.scale(imagen_demasiado_quieto, (90, 110))
                # self.image.set_colorkey(NEGRO)
                # self.indice_demasiado_quieto += 1
                # tiempo_transcurrido = 0


        if self.rect.left < 0:
            self.rect.left = 0

        elif self.rect.right > ANCHO:
            self.rect.right = ANCHO






pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('One piece 5-Days')
clock = pygame.time.Clock()

jugador = Jugador()

luffy = pygame.sprite.Group()

luffy.add(jugador)


jugando = True
while jugando:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    pantalla.fill(NEGRO)
    luffy.update()
    luffy.draw(pantalla)
    pygame.display.flip()

pygame.quit

