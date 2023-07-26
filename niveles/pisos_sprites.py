import pygame

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

BACKGROUND_X = 0

class Piso(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def update(self):
        global BACKGROUND_X
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            BACKGROUND_X += 10

    def piso(self, x, y, ruta_sprite):

        self.image = pygame.image.load(ruta_sprite).convert()
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.bottom = y
        # return self.rect

    # def movimiento_piso(self,x):
    #     self.rect.x -= x


    
    def prueba(self):
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

        piso_2 = Piso()
        piso_2.piso(piso_1.rect.width, ALTO, imagen_piso2)

        piso_3 = Piso()
        piso_3.piso(piso_2.rect.width, ALTO, imagen_piso3)

        piso_4 = Piso()
        piso_4.piso(piso_3.rect.width, ALTO, imagen_piso4)

        grupo_sprite_piso = pygame.sprite.Group()
        grupo_sprite_piso.add(piso_1)
        grupo_sprite_piso.add(piso_2)
        grupo_sprite_piso.add(piso_3)
        grupo_sprite_piso.add(piso_4)

        return grupo_sprite_piso


if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode((1005, ALTO))
    pygame.display.set_caption('prueba fondo sprites')

    imagen_piso1 = '../recursos/imagenes/Alvidapiso1.jpg'
    imagen_piso2 = '../recursos/imagenes/Alvidapiso2.jpg'
    imagen_piso3 = '../recursos/imagenes/Alvidapiso3.jpg'
    imagen_piso4 = '../recursos/imagenes/Alvidapiso4.jpg'
    imagen_piso5 = '../recursos/imagenes/Alvidapiso5.jpg'
    imagen_piso6 = '../recursos/imagenes/Alvidapiso6.jpg'
    imagen_piso7 = '../recursos/imagenes/Alvidapiso7.jpg'
    imagen_piso8 = '../recursos/imagenes/Alvidapiso8.jpg'



    pantalla.fill(NEGRO)
    
    piso_1 = Piso()
    piso_1.piso(0, ALTO, imagen_piso1)

    piso_2 = Piso()
    piso_2.piso(piso_1.rect.width, ALTO, imagen_piso2)

    piso_3 = Piso()
    piso_3.piso(piso_2.rect.width, ALTO, imagen_piso3)

    piso_4 = Piso()
    piso_4.piso(piso_3.rect.width, ALTO, imagen_piso4)

    grupo_sprite_piso = pygame.sprite.Group()
    grupo_sprite_piso.add(piso_1)
    grupo_sprite_piso.add(piso_2)
    grupo_sprite_piso.add(piso_3)
    grupo_sprite_piso.add(piso_4)

    jugando = True
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False

            grupo_sprite_piso.draw(pantalla)
            grupo_sprite_piso.update()
            # pantalla.blit((BACKGROUND_X, 0))
            pygame.display.flip()
