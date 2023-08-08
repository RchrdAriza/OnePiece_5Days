import pyglet
import pygame
from pygame.locals import *

# Configurar Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Reproducir Video en Pygame')

# Cargar el video con pyglet
video_path = '../recursos/imagenes/cinematica1.mp4'
player = pyglet.media.Player()
source = pyglet.media.load(video_path)
player.queue(source)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Actualizar la pantalla de Pygame
    screen.fill((0, 0, 0))

    # Actualizar el reproductor de pyglet
    player.dispatch_events()
    if player.playing:
        player.get_texture().blit(0, 0)

    pygame.display.flip()

pygame.quit()

