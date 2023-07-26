import pygame

FONDO_ANCHO = 2738
FONDO_ALTO = 600

ANCHO = 800
ALTO = 600

FPS = 30

NEGRO = (0, 0, 0)

BACKGROUND_X = 0

class Piso(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def update(self):
        global BACKGROUND_X
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            BACKGROUND_X += 10
            for sprite in grupo_sprite_piso:
                sprite.rect.x -= 10
                print(sprite)

    def piso(self, x, y, ruta_sprite):
        self.image = pygame.image.load(ruta_sprite).convert()
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.bottom = y


if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode((1005, ALTO))
    pygame.display.set_caption('prueba fondo sprites')

    pantalla.fill(NEGRO)

    # ... (Your sprite creation code here)
    imagen_piso1 = '../recursos/imagenes/Alvidapiso1.jpg'
    imagen_piso2 = '../recursos/imagenes/Alvidapiso2.jpg'
    imagen_piso3 = '../recursos/imagenes/Alvidapiso3.jpg'
    imagen_piso4 = '../recursos/imagenes/Alvidapiso4.jpg'
    imagen_piso5 = '../recursos/imagenes/Alvidapiso5.jpg'
    imagen_piso6 = '../recursos/imagenes/Alvidapiso6.jpg'
    imagen_piso7 = '../recursos/imagenes/Alvidapiso7.jpg'
    imagen_piso8 = '../recursos/imagenes/Alvidapiso8.jpg'



    # pantalla.fill(NEGRO)
    
    piso_1 = Piso()
    piso_1.piso(0, ALTO, imagen_piso1)

    piso_2 = Piso()
    piso_2.piso(piso_1.rect.width, ALTO, imagen_piso2)
    piso_acumulativa = piso_1.rect.width

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

    grupo_sprite_piso = pygame.sprite.Group()
    grupo_sprite_piso.add(piso_1)
    grupo_sprite_piso.add(piso_2)
    grupo_sprite_piso.add(piso_3)
    grupo_sprite_piso.add(piso_4)
    grupo_sprite_piso.add(piso_5)
    grupo_sprite_piso.add(piso_6)
    grupo_sprite_piso.add(piso_7)
    grupo_sprite_piso.add(piso_8)

    jugando = True
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False

        grupo_sprite_piso.update()

        pantalla.fill(NEGRO)  # Clear the screen with black color before drawing the sprites

        grupo_sprite_piso.draw(pantalla)

        pygame.display.flip()

