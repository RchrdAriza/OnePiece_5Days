import pygame

NEGRO = (0, 0, 0)
class Objecto(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.x = x
        # self.y = y

    def update(self):
        pass

    def objecto(self, x, y, ruta_imagen):
        if type(ruta_imagen) == list:
            for rutas in ruta_imagen:
                self.image = pygame.image.load(rutas).convert()
                self.image.set_colorkey(NEGRO)
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
        else:
            self.image = pygame.image.load(ruta_imagen).convert()
            self.image.set_colorkey(NEGRO)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y


