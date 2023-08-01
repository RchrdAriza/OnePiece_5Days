import pygame, time
# from pygame.locals import *

ANCHO = 800
ALTO = 600

# FONDO_ANCHO = 2738
# FONDO_ALTO = 600

FPS = 30

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
H_FA2F2F = (255, 47, 47)
VERDE = (0, 255, 0)
AZUL = (0,0, 255)
AZUL2 = (64, 64, 255)
H_50D2FE = (94, 210, 254)
# GRAVEDAD = 1
# BACKGROUND_X = 0

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('../recursos/imagenes/quieto.png').convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        # self.rect.center = (0, 500)
        self.rect.x = 0
        self.posicion_x = 0
        self.salto_altura = 0
        self.gravedad = 1

        self.correr_lista = [pygame.image.load("../recursos/imagenes/Run1.png"),
                             pygame.image.load("../recursos/imagenes/Run2.png"),
                             pygame.image.load("../recursos/imagenes/Run3.png"),
                             pygame.image.load("../recursos/imagenes/Run4.png"),
                             pygame.image.load("../recursos/imagenes/Run5.png"),
                             pygame.image.load("../recursos/imagenes/Run6.png"),
                             pygame.image.load("../recursos/imagenes/Run7.png"),
                             pygame.image.load("../recursos/imagenes/Run8.png"),]
        # quedarse dormido

        self.demasiado_quieto_secuencia = [pygame.image.load('../recursos/imagenes/Demasiadoquieto1.png'),
                                        pygame.image.load('../recursos/imagenes/Demasiadoquieto2.png'),
                                        pygame.image.load('../recursos/imagenes/Demasiadoquieto3.png'),
                                        pygame.image.load('../recursos/imagenes/Demasiadoquieto4.png'),
                                        pygame.image.load('../recursos/imagenes/Demasiadoquieto5.png'),]

        # Salto

        self.salto_secuencia  = [pygame.image.load('../recursos/imagenes/Salto1.png'),
                                 pygame.image.load('../recursos/imagenes/Salto2.png'),
                                 pygame.image.load('../recursos/imagenes/Salto3.png'),
                                 pygame.image.load('../recursos/imagenes/Salto4.png'),]

        # Primer_ataque

        self.primer_ataque_secuencia = [pygame.image.load('../recursos/imagenes/Primerataque1.png'),
                                        pygame.image.load('../recursos/imagenes/Primerataque2.png'),
                                        pygame.image.load('../recursos/imagenes/Primerataque3.png'),
                                        pygame.image.load('../recursos/imagenes/Primerataque4.png'),]
        
        # correr
        self.indice_correr = 0
        self.velocidad_correr = 3
        
        # demasiado_quieto
        self.indice_demasiado_quieto = 0
        self.velocidad_secuencia_demasiado_quieto = 5

        # Salto
        self.velocidad_salto = 40
        self.indice_salto = 0

        # Movimiento
        self.movimiento_derecha = False
        self.movimiento_izquierda = False
        # self.tiempo_inicial = time.time()

        # primer ataque
        self.velocidad_secuencia_primer_ataque = 3
        self.indice_primer_ataque = 0

    def update(self):
        pass 

        # self.posicion_x = 0

    # tiempo_transcurrido = time.time() - self.tiempo_inicial
    global BACKGROUND_X
    
    # teclas = pygame.key.get_pressed()
    def correr_derecha(self):
        self.indice_correr += 1
        if self.indice_correr == len(self.correr_lista) * self.velocidad_correr:
            self.indice_correr = 0
        imagen_actual = self.correr_lista[self.indice_correr // self.velocidad_correr]


        # Actualizar la imagen del jugador
        # self.image = pygame.transform.scale(imagen_actual, (90, 110))
        self.image = imagen_actual
        self.image.set_colorkey(NEGRO)
        # self.posicion_x += 10
        self.rect.x += 5
        # self.movimiento_derecha = True
        if self.rect.left < 0:
            self.rect.left = 0

        elif self.rect.right > ANCHO:
            self.rect.right = ANCHO


    # else:
    #     self.movimiento_derecha = False
    def correr_izquierda(self):
        if self.indice_correr == len(self.correr_lista) * self.velocidad_correr:
            self.indice_correr = 0
        imagen_actual = self.correr_lista[self.indice_correr // self.velocidad_correr]
        imagen_volteada_horizontalmente = pygame.transform.flip(imagen_actual, True, False)


        # Actualizar la imagen del jugador
        # self.image = pygame.transform.scale(imagen_volteada_horizontalmente, (90, 110))
        self.image = imagen_volteada_horizontalmente
        self.image.set_colorkey(NEGRO)
        # self.posicion_x += 10
        self.rect.x -= 5
        self.movimiento_izquierda = True
        self.indice_correr += 1
        
        if self.rect.left < 0:
            self.rect.left = 0

        elif self.rect.right > ANCHO:
            self.rect.right = ANCHO


    #
    def quieto(self):
        quieto_img = pygame.image.load('../recursos/imagenes/quieto.png').convert()
        quieto_img.set_colorkey(NEGRO)
        self.image = quieto_img

    def quieto_volteado(self):
            quieto_img = pygame.image.load('../recursos/imagenes/quieto.png').convert()
            quieto_img_volteado = pygame.transform.flip(quieto_img, True, False)
            quieto_img_volteado.set_colorkey(NEGRO)
            self.image = quieto_img_volteado



    def saltar(self):
        # salto_animacion = pygame.transform.scale()
        # for _ in range(3):
        # self.rect = self.image.get_rect()
        for _ in range(10):
            self.rect.y -= 9.8
            
        # print("hello world")
    
    def durante_el_salto(self):

        if self.indice_salto == len(self.salto_secuencia) * self.velocidad_salto:
            self.indice_salto = 0
        imagen_actual = self.salto_secuencia[self.indice_salto // self.velocidad_salto]


        # Actualizar la imagen del jugador
        self.image = pygame.transform.scale(imagen_actual, (90, 110))
        self.image.set_colorkey(NEGRO)

        self.indice_salto += 1

    def demasiado_quieto(self):

             if self.indice_demasiado_quieto == len(self.demasiado_quieto_secuencia) * self.velocidad_secuencia_demasiado_quieto: 
                 self.indice_demasiado_quieto = 0 
             imagen_demasiado_quieto = self.demasiado_quieto_secuencia[self.indice_demasiado_quieto // self.velocidad_secuencia_demasiado_quieto] 
             self.image = pygame.transform.scale(imagen_demasiado_quieto, (90, 110)) 
             self.image.set_colorkey(NEGRO) 

             self.indice_demasiado_quieto += 1 

    def primer_ataque(self):
        
        # self.indice_primer_ataque += 1
        if self.indice_primer_ataque == len(self.primer_ataque_secuencia) * self.velocidad_secuencia_primer_ataque:
            self.indice_primer_ataque = 0
        imagen_actual = self.primer_ataque_secuencia[self.indice_primer_ataque // self.velocidad_secuencia_primer_ataque]

        self.image = imagen_actual
        # self.image = pygame.transform.scale(imagen_actual, (90, 110)) 
        self.image.set_colorkey(NEGRO)
        self.indice_primer_ataque += 1



#
#
if __name__ == "__main__":
    
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('One piece 5-Days')
    clock = pygame.time.Clock()
    #
    jugador = Jugador()

    luffy = pygame.sprite.Group()

    luffy.add(jugador)
    #
    #
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
    #
