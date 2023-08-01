# Importar pygame
import pygame

# Inicializar pygame
pygame.init()

# Crear una pantalla de 800x600 píxeles
screen = pygame.display.set_mode((800, 600))

# Crear un reloj para controlar el tiempo
clock = pygame.time.Clock()

# Crear dos rectángulos con colores y tamaños diferentes
A = pygame.Rect(400, 300, 100, 50)
A_color = (255, 0, 0) # Rojo

B = pygame.Rect(200, 150, 50, 100)
B_color = (0, 0, 255) # Azul

# Crear una variable para el bucle principal
running = True

# Bucle principal
while running:
    # Limitar el bucle a 60 fotogramas por segundo
    clock.tick(60)

    # Procesar los eventos de entrada
    for event in pygame.event.get():
        # Si se cierra la ventana, salir del bucle
        if event.type == pygame.QUIT:
            running = False

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Mover el rectángulo A con las flechas izquierda y derecha
    if keys[pygame.K_LEFT]:
        A.x -= 5
    if keys[pygame.K_RIGHT]:
        A.x += 5

    # Mover el rectángulo B con las flechas arriba y abajo
    if keys[pygame.K_UP]:
        B.y -= 5
    if keys[pygame.K_DOWN]:
        B.y += 5

    # Obtener los puntos medios de los cuatro lados de los rectángulos
    punto_izq_A = A.midleft
    punto_der_A = A.midright
    punto_arr_A = A.midtop
    punto_aba_A = A.midbottom

    punto_izq_B = B.midleft
    punto_der_B = B.midright
    punto_arr_B = B.midtop
    punto_aba_B = B.midbottom

    # Comprobar si hay colisión entre los lados de los rectángulos
    if B.collidepoint(punto_izq_A):
        # Hay colisión por el lado izquierdo de A
        # Cambiar el color de fondo a rojo
        screen.fill((255, 0, 0))

    elif B.collidepoint(punto_der_A):
        # Hay colisión por el lado derecho de A
        # Cambiar el color de fondo a verde
        screen.fill((0, 255, 0))

    elif B.collidepoint(punto_arr_A):
        # Hay colisión por el lado superior de A
        # Cambiar el color de fondo a azul
        screen.fill((0, 0, 255))

    elif B.collidepoint(punto_aba_A):
        # Hay colisión por el lado inferior de A
        # Cambiar el color de fondo a amarillo
        screen.fill((255, 255, 0))

    elif A.collidepoint(punto_izq_B):
        # Hay colisión por el lado izquierdo de B
        # Cambiar el color de fondo a cian
        screen.fill((0, 255, 255))

    elif A.collidepoint(punto_der_B):
        # Hay colisión por el lado derecho de B
        # Cambiar el color de fondo a magenta
        screen.fill((255, 0, 255))

    elif A.collidepoint(punto_arr_B):
        # Hay colisión por el lado superior de B
        # Cambiar el color de fondo a naranja
        screen.fill((255, 165, 0))

    elif A.collidepoint(punto_aba_B):
        # Hay colisión por el lado inferior de B
        # Cambiar el color de fondo a morado
        screen.fill((128, 0, 128))

    # Si no hay colisión, mantener el color de fondo blanco
    else:
        screen.fill((255, 255, 255))

    # Dibujar los rectángulos en la pantalla con sus respectivos colores
    pygame.draw.rect(screen, A_color, A)
    pygame.draw.rect(screen, B_color, B)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de pygame
pygame.quit()

