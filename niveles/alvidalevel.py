import pygame
import sys
sys.path.append("..")
from personajes.luffy import Jugador
from pisos_sprites import Piso

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
inactividad = 0
# en_movimiento = False

class Alvidalevel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.GRAVEDAD = 9.8
        self.velocidad_caida = 0
        self.contador_inactividad = 1

    def update(self):
        self.en_movimiento_derecha = False
        self.en_movimiento_izquierda = False
        self.enElSuelo = False
        self.colision_lateral_x_positiva = False
        self.colision_lateral_x_negativa = False

        global background_x
        global inactividad
        global jugador

        variable_aumentadora_sprite = 0
        for sprite in grupos_sprite_piso:
            if jugador.rect.colliderect(sprite.rect):
                self.GRAVEDAD = 0
                self.enElSuelo = True
                # print(self.enElSuelo)


            if variable_aumentadora_sprite > 6:
                variable_aumentadora_sprite = 0
            #
            if jugador.rect.colliderect(grupos_sprite_piso[variable_aumentadora_sprite]) and jugador.rect.colliderect(grupos_sprite_piso[variable_aumentadora_sprite + 1]):
                self.colision_lateral_x_positiva = True
            variable_aumentadora_sprite += 1
            #
        key = pygame.key.get_pressed()
        if key[pygame.K_d] and not self.colision_lateral_x_positiva:
            background_x -= 10
            jugador.correr_derecha()
            if derecha.right > ANCHO + 5:
                for sprite in sprites_piso:
                    sprite.rect.x -= 10
            self.en_movimiento_derecha = True
            inactividad = 0

            
            

        if key[pygame.K_a] and not self.colision_lateral_x_negativa:
            background_x += 10
            jugador.correr_izquierda()
            self.en_movimiento_izquierda = True
            if izquierda.left > 0:
                for sprite in sprites_piso:
                    sprite.rect.x += 10
            elif izquierda.left < 0 and derecha.right < FONDO_ANCHO:
                for sprite in sprites_piso:
                    sprite.rect.x += 10
            inactividad = 0

        if key[pygame.K_w] and self.enElSuelo:
            # print("hola mundo")
            jugador.rect.x -= 5
            jugador.saltar()
            inactividad = 0

        if not self.enElSuelo:
            jugador.durante_el_salto()


            

        if not self.en_movimiento_derecha and not self.en_movimiento_izquierda and self.enElSuelo:
            if inactividad < 500:
                jugador.quieto()
            else:
                jugador.demasiado_quieto()
            print(inactividad)




        jugador.rect.y += self.GRAVEDAD

            

        inactividad += self.contador_inactividad
        if background_x > 0:
            background_x = 0

        limite_derecho = FONDO_ANCHO - ANCHO
        if background_x < -limite_derecho:
            background_x = -limite_derecho


def pisos():
        imagen_piso1 = '../recursos/imagenes/Alvidapiso1.jpg'
        imagen_piso2 = '../recursos/imagenes/Alvidapiso2.jpg'
        imagen_piso3 = '../recursos/imagenes/Alvidapiso3.jpg'
        imagen_piso4 = '../recursos/imagenes/Alvidapiso4.jpg'
        imagen_piso5 = '../recursos/imagenes/Alvidapiso5.jpg'
        imagen_piso6 = '../recursos/imagenes/Alvidapiso6.jpg'
        imagen_piso7 = '../recursos/imagenes/Alvidapiso7.jpg'
        imagen_piso8 = '../recursos/imagenes/Alvidapiso8.jpg'

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

        return sprites_piso, piso_1.rect, piso_8.rect




if __name__ == "__main__":

    pygame.init()
    clock = pygame.time.Clock()
    pantalla1 = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Level: 01')
    imagen_fondo = pygame.image.load('../recursos/imagenes/alvidabarcodentro.jpg')
    sprites_piso, izquierda, derecha = pisos()
    grupos_sprite_piso = sprites_piso.sprites()
    nivel1 = Alvidalevel()
    jugador = Jugador()
    # jugador_imagen = jugador.imagen_rect()
    luffy = pygame.sprite.Group()
    luffy.add(jugador)
    while nivel1:
        clock.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                nivel1 = False
        
        pantalla1.blit(imagen_fondo, (background_x, 0))
        # pantalla1.fill(NEGRO)
        alvida = Alvidalevel()
        sprites_piso.update()
        sprites_piso.draw(pantalla1)
        alvida.update()
        luffy.draw(pantalla1)
        luffy.update()
        pygame.display.flip()


    pygame.quit


