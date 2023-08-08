import pygame

pygame.init()

# Crear ventana
ventana = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtener posición del mouse
            pos = pygame.mouse.get_pos()
            print("Posición del mouse:", pos)

            # Detectar clic en botón izquierdo del mouse
            if event.button == 1:
                print("Clic en botón izquierdo del mouse")

