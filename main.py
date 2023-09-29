import pygame
from niveles.alvidalevel import main
import sys
import os

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menú de Juego")

# Cargar la imagen de fondo
# Reemplaza "fondo.png" con la ruta de tu imagen de fondo
background = pygame.image.load("./recursos/imagenes/fondo.jpg")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Musica
pygame.mixer_music.load("./recursos/musica/theme.wav")

pygame.mixer_music.play(-1)

# Cambia "tu_fuente.ttf" por el nombre de tu archivo TTF
font_path = os.path.join("fonts", "one_piece_font.ttf")
font_size = 40
font = pygame.font.Font(font_path, font_size)


def draw_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)


def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Aquí puedes agregar la lógica para iniciar el juego
                    main()

        # Dibujar la imagen de fondo
        screen.blit(background, (0, 0))

        draw_text("¡Bienvenido al Juego!", screen_width //
                  2, screen_height // 4, black)
        draw_text("Presiona ENTER para empezar",
                  screen_width // 2, screen_height // 2, black)
        pygame.display.update()


if __name__ == "__main__":
    main_menu()
