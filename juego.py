import pygame
import sys
from niveles.alvidalevel import main
from niveles.pisos_sprites import Piso
pygame.init()


# Dimensiones de la ventana
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Ejemplo de Menú')

# Función para mostrar texto en la ventana
def mostrar_texto(texto, fuente, color, x, y):
    superficie_texto = fuente.render(texto, True, color)
    ventana.blit(superficie_texto, (x, y))

# Función para mostrar el menú
def mostrar_menu():
    fuente = pygame.font.Font(None, 30)
    opciones = ["Opción 1", "Opción 2", "Opción 3"]
    seleccionado = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    seleccionado = (seleccionado - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    seleccionado = (seleccionado + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    main()
                    print(f"Has seleccionado: {opciones[seleccionado]}")

        ventana.fill(BLANCO)
        for i, opcion in enumerate(opciones):
            color = AZUL if i == seleccionado else NEGRO
            mostrar_texto(opcion, fuente, color, ANCHO // 2 - 50, ALTO // 2 + i * 40)

        pygame.display.flip()
    pygame.quit()

# Iniciar el menú
mostrar_menu()
