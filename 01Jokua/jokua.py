import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de Tenis en Python")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255,0,0)

# Jugadores
player1_width, player1_height = 10, 100
player2_width, player2_height = 10, 100
player1_x, player2_x = 50, width - 50 - player2_width
player1_y, player2_y = height // 2 - player1_height // 2, height // 2 - player2_height // 2
player1_speed, player2_speed = 1, 1

# Pelota
ball_width, ball_height = 10, 10
ball_x, ball_y = width // 2 - ball_width // 2, height // 2 - ball_height // 2
ball_speed_x, ball_speed_y = 0.3 * random.choice((1, -1)), 0.3 * random.choice((1, -1))

# Puntuación
score1, score2 = 0, 0
font = pygame.font.Font(None, 36)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= player1_speed
    if keys[pygame.K_s] and player1_y < height - player1_height:
        player1_y += player1_speed
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= player2_speed
    if keys[pygame.K_DOWN] and player2_y < height - player2_height:
        player2_y += player2_speed

    # Actualizar la posición de la pelota
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Colisiones con las paletas
    if (
        ball_x <= player1_x + player1_width
        and player1_y < ball_y < player1_y + player1_height
    ):
        ball_speed_x = abs(ball_speed_x)
    if (
        ball_x >= player2_x - ball_width
        and player2_y < ball_y < player2_y + player2_height
    ):
        ball_speed_x = -abs(ball_speed_x)

    # Colisiones con las paredes superior e inferior
    if ball_y <= 0 or ball_y >= height - ball_height:
        ball_speed_y = -ball_speed_y

    # Puntuación
    if ball_x < 0:
        score2 += 1
        ball_x, ball_y = width // 2 - ball_width // 2, height // 2 - ball_height // 2
        ball_speed_x, ball_speed_y = 0.3 * random.choice((1, -1)), 0.3 * random.choice((1, -1))
    elif ball_x > width:
        score1 += 1
        ball_x, ball_y = width // 2 - ball_width // 2, height // 2 - ball_height // 2
        ball_speed_x, ball_speed_y = 0.3 * random.choice((1, -1)), 0.3 * random.choice((1, -1))

    # Limpiar la pantalla
    screen.fill(black)

    # Dibujar paletas y pelota
    pygame.draw.rect(screen, white, (player1_x, player1_y, player1_width, player1_height))
    pygame.draw.rect(screen, white, (player2_x, player2_y, player2_width, player2_height))
    pygame.draw.ellipse(screen, red, (ball_x, ball_y, ball_width, ball_height))

    # Dibujar puntuación
    text1 = font.render(f"Jugador 1: {score1}", True, white)
    text2 = font.render(f"Jugador 2: {score2}", True, white)
    screen.blit(text1, (20, 20))
    screen.blit(text2, (width - 180, 20))

    # Actualizar la pantalla
    pygame.display.update()

    if(score1 or score2 > 3):
        sys.exit()

# Salir del juego
pygame.quit()
sys.exit()
