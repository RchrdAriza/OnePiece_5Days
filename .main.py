import pygame
import sys
from niveles.alvidalevel import main
import os

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menú de Juego")

# Cargar la imagen de fondo
background = pygame.image.load("./recursos/imagenes/fondo.jpg")  # Reemplaza "fondo.png" con la ruta de tu imagen de fondo

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
AZUL = (0, 0, 255)

# Fuente para el texto

font_path = os.path.join("fonts", "one_piece_font.ttf")  # Cambia "tu_fuente.ttf" por el nombre de tu archivo TTF
font_size = 40
font = pygame.font.Font(font_path, font_size)


def draw_text_with_background(text, x, y, text_color, bg_color):
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)

    # Calcular el tamaño del fondo basado en el tamaño del texto
    bg_width = text_rect.width + 20
    bg_height = text_rect.height + 10
    bg_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 5, bg_width, bg_height)

    # Dibujar el fondo blanco
    pygame.draw.rect(screen, bg_color, bg_rect)
    
    # Dibujar el texto en la parte superior del fondo
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

        # Dibujar el texto con fondo blanco
        draw_text_with_background("Start your adventure!", screen_width // 2, screen_height // 4, black, white)
        draw_text_with_background("Press enter to play :)", screen_width // 2, screen_height // 2, black, white)
        pygame.display.update()

if __name__ == "__main__":
    main_menu()

