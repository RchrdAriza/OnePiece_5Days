import pygame
# import sys
# sys.path.append("..")
from personajes.luffy import Jugador
from .pisos_sprites import Piso
from .obtaculos_y_enemigos.objectos_sprites import Objecto
from .nivel2 import main1

# Variables CONSTANTES que utilizo
FONDO_ANCHO = 2738
FONDO_ALTO = 600

# Dimensiones de la ventana
ANCHO = 800
ALTO = 600

# Tasa de Frames por segundo
FPS = 30

# Colores RGB
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
H_FA2F2F = (255, 47, 47)
VERDE = (0, 255, 0)
AZUL = (0,0, 255)
AZUL2 = (64, 64, 255)
H_50D2FE = (94, 210, 254)

background_x = 0
INACTIVIDAD = 0
VOLTEADO = False


class Alvidalevel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.GRAVEDAD = 9.8
        self.contador_inactividad = 1
        # self.prueba = 0

    def update(self):

        self.en_movimiento_derecha = False
        self.en_movimiento_izquierda = False
        self.enElSuelo = False
        self.colision_lateral_x_positiva = False
        self.colision_lateral_x_negativa = False
        self.atacando = False
        self.colision_saltando = False

        global background_x
        global INACTIVIDAD
        global VOLTEADO

        variable_aumentadora_sprite = 0

        jugador_bottom = jugador.rect.midbottom

        for sprite in grupos_sprite_piso:

            if variable_aumentadora_sprite > 6:
                variable_aumentadora_sprite = 0

            # verifica si el jugador esta tocando el piso
            if sprite.rect.collidepoint(jugador_bottom):
                self.GRAVEDAD = 0
                self.enElSuelo = True

            # verifica si el jugador esta chocando con un obtaculo del piso (debo mejorarla)
            if jugador.rect.colliderect(grupos_sprite_piso[variable_aumentadora_sprite]) and jugador.rect.colliderect(grupos_sprite_piso[variable_aumentadora_sprite + 1]):
                # jugador.rect.x += 1
                self.colision_lateral_x_positiva = True

            if not self.enElSuelo and jugador.rect.colliderect(sprite):
                # print("hola mundo")
                self.colision_saltando = True

            # Variables acumuladora que me permite iterar sobre distintos sobre distintos sprites sin usar bucle for
            variable_aumentadora_sprite += 1


        # En caso de que no esté en el suelo llama la funcion enElAire de la clase jugador
        if not self.enElSuelo:
            jugador.enElAire()



        # detecta las teclas presionadas y las almacena en la variable key
        key = pygame.key.get_pressed()

        # si el usuario presiona x realiza el primer ataque
        if key[pygame.K_x]:
            jugador.primer_ataque()
            self.atacando = True
            INACTIVIDAD = 0


        # si el usuario presiona d y no esta chocando con nada entonces avanza
        if key[pygame.K_d] and not self.colision_lateral_x_positiva and not self.colision_saltando:
            background_x -= 10
            jugador.correr_derecha()
            if derecha.right > ANCHO + 5:
                for sprite in sprites_piso:
                    sprite.rect.x -= 10
            self.en_movimiento_derecha = True

            for objectos in sprite_objectos:
                objectos.rect.x -= 10

            INACTIVIDAD = 0
            VOLTEADO = False

        # retrocede
        if key[pygame.K_a]:

            background_x += 10
            jugador.correr_izquierda()
            self.en_movimiento_izquierda = True
            for sprite in sprites_piso:
                if izquierda.left > 0:
                    sprite.rect.x += 10
                elif izquierda.left < 0 and derecha.right < FONDO_ANCHO:
                        sprite.rect.x += 10
            for objectos in sprite_objectos:
                objectos.rect.x += 10

            INACTIVIDAD = 0
            VOLTEADO = True

        # W para saltar
        if key[pygame.K_w] and self.enElSuelo:
            jugador.saltar()
            INACTIVIDAD = 0


        if not self.en_movimiento_derecha and not self.en_movimiento_izquierda and self.enElSuelo and not VOLTEADO and not self.atacando:
            if INACTIVIDAD < 500:
                jugador.quieto()
            else:
            # Si demora mas de 500 iteraciones sin relaizar nada comienza la animacion de dormido
                jugador.demasiado_quieto()


        if not self.en_movimiento_derecha and not self.en_movimiento_izquierda and self.enElSuelo and VOLTEADO and not self.atacando:
            if INACTIVIDAD < 500:
                jugador.quieto_volteado()
            else:
                jugador.demasiado_quieto()


        jugador.rect.y += self.GRAVEDAD


        INACTIVIDAD += self.contador_inactividad


        if background_x > 0:
            background_x = 0

        limite_derecho = FONDO_ANCHO - ANCHO
        if background_x < -limite_derecho:
            background_x = -limite_derecho

# funcion que cargar y coloca los sprites que simulan el suelo
def pisos():

        imagen_piso1 = 'recursos/imagenes/Alvidapiso1.jpg'
        imagen_piso2 = 'recursos/imagenes/Alvidapiso2.jpg'
        imagen_piso3 = 'recursos/imagenes/Alvidapiso3.jpg'
        imagen_piso4 = 'recursos/imagenes/Alvidapiso4.jpg'
        imagen_piso5 = 'recursos/imagenes/Alvidapiso5.jpg'
        imagen_piso6 = 'recursos/imagenes/Alvidapiso6.jpg'
        imagen_piso7 = 'recursos/imagenes/Alvidapiso7.jpg'
        imagen_piso8 = 'recursos/imagenes/Alvidapiso8.jpg'

        piso_1 = Piso()
        piso_1.piso(0, ALTO, imagen_piso1)
        piso_acumulativa = piso_1.rect.width
        piso_1.rect

        piso_2 = Piso()
        piso_2.piso(piso_acumulativa, ALTO, imagen_piso2)
        piso_acumulativa += piso_2.rect.width

        piso_3 = Piso()
        piso_3.piso(piso_acumulativa, ALTO, imagen_piso3)
        piso_acumulativa += piso_3.rect.width

        piso_4 = Piso()
        piso_4.piso(piso_acumulativa, ALTO, imagen_piso4)
        piso_acumulativa += piso_4.rect.width

        piso_5 = Piso()
        piso_5.piso(piso_acumulativa, ALTO, imagen_piso5)
        piso_acumulativa += piso_5.rect.width

        piso_6 = Piso()
        piso_6.piso(piso_acumulativa, ALTO, imagen_piso6)
        piso_acumulativa += piso_6.rect.width

        piso_7 = Piso()
        piso_7.piso(piso_acumulativa, ALTO, imagen_piso7)
        piso_acumulativa += piso_7.rect.width

        piso_8 = Piso()
        piso_8.piso(piso_acumulativa, ALTO, imagen_piso8)
        piso_acumulativa += piso_8.rect.width

        sprites_piso = pygame.sprite.Group()
        sprites_piso.add(piso_1)
        sprites_piso.add(piso_2)
        sprites_piso.add(piso_3)
        sprites_piso.add(piso_4)
        sprites_piso.add(piso_5)
        sprites_piso.add(piso_6)
        sprites_piso.add(piso_7)
        sprites_piso.add(piso_8)

        # Retorna el grupo de sprite que controla los pisos, ademas del primer y ultimo sprite
        return sprites_piso, piso_1.rect, piso_8.rect

def objetos():

    puerta = Objecto()
    imagen_puerta = 'recursos/imagenes/Puerta1.png'
    puerta.objecto(240, 400 - 150, imagen_puerta)

    sprite_objectos = pygame.sprite.Group()

    sprite_objectos.add(puerta)

    return sprite_objectos

def Notificaciones():

    x = Objecto()
    imagen_x = ['recursos/imagenes/Pressup1.png']
    x.objecto(ANCHO - 170, 15, imagen_x)

    notificaciones_sprite = pygame.sprite.Group()

    notificaciones_sprite.add(x)

    return notificaciones_sprite



def main():

    global sprites_piso, izquierda, derecha, jugador, grupos_sprite_piso, sprite_objectos

    # Contador de FPS's
    clock = pygame.time.Clock()

    # Configuracion basica de la pantalla (tamaño, nombre, fondo)
    pantalla1 = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Level: 01')
    imagen_fondo = pygame.image.load('recursos/imagenes/alvidabarcodentro.jpg')

    # Grupo de sprites (Pisos, Jugador y obtaculos)
    sprites_piso, izquierda, derecha = pisos()
    grupos_sprite_piso = sprites_piso.sprites()
    sprite_objectos = objetos()
    notificaciones_sprite = Notificaciones()
    jugador = Jugador()
    luffy = pygame.sprite.Group()
    luffy.add(jugador)

    # Bucle principal del juego
    nivel1 = True
    while nivel1:

        clock.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                nivel1 = False

        pantalla1.blit(imagen_fondo, (background_x, 0))
        # pantalla1.fill(NEGRO)

        # inicializacion y actualizacion de los objectos en pantalla
        sprites_piso.update()
        sprites_piso.draw(pantalla1)

        sprite_objectos.update()
        sprite_objectos.draw(pantalla1)

        keys = pygame.key.get_pressed()
        if pygame.sprite.groupcollide(luffy, sprite_objectos, False, False):
            notificaciones_sprite.update()
            notificaciones_sprite.draw(pantalla1)

            if keys[pygame.K_UP]:
                main1()

        luffy.draw(pantalla1)
        luffy.update()

        alvida = Alvidalevel()
        alvida.update()
        pygame.display.flip()


    pygame.quit()


if __name__ == "__main__":

    main()
