import pygame
import random
import math
import time
from pygame import mixer

pygame.init()
# display
display = pygame.display.set_mode((1350, 730))
# name
pygame.display.set_caption("FLYCYCLE")
# logo
logo = pygame.image.load('.png\\cycle.png')
pygame.display.set_icon(logo)
# background
back_image = pygame.image.load('.png\\background.png')
# background music
mixer.music.load('.wav\\background music.wav')
mixer.music.play(-1)

# cycle
cycle = pygame.image.load('.png\\cycle.png')
cx = 0
cy = 365
cx_c = 0
cy_c = 0


def c_fun(x, y):
    display.blit(cycle, (x, y))


# ostacales
obstacales = []
ox = []
oy = []
ox_c = []
no_of_obstacales = 15
for i in range(no_of_obstacales):
    obstacales.append(pygame.image.load('.png\\obstacales.png'))
    ox.append(random.randint(128, 1286))
    oy.append(random.randint(20, 666))
    ox_c.append(-2)


def o_fun(x, y):
    display.blit(obstacales[i], (x, y))


# collusion

def collusion_fun(cx, cy, ox, oy):
    distance = math.sqrt((math.pow(cx - ox, 2)) + (math.pow(cy - oy, 2)))

    if distance < 64:
        return True
    else:
        return False


# time limit
start_time = time.time()
time_limit_value = 120
time_limit_text = pygame.font.Font('.ttf\\Pacifico.ttf', 50)


def t_fun():
    time_limit = time_limit_text.render('Time Left: ' + str(final_time), True, (0, 0, 0))
    display.blit(time_limit, (1120, 0))


# game over
def g_fun():
    game_over_text = pygame.font.Font('.ttf\\Pacifico.ttf', 128)
    game_over = game_over_text.render('Game Over', True, (54, 4, 4))
    display.blit(game_over, (340, 260))


# win
win_text = pygame.font.Font('.ttf\\Pacifico.ttf', 128)


def w_fun():
    win = win_text.render(' You Win', True, (35, 6, 51))
    display.blit(win, (340, 260))


running = True
while running:
    pygame.display.update()

    display.blit(back_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # cycle music
            # cycle_sound=mixer.sound('cycle sound.wav')
            # cycle_sound.play()

            if event.key == pygame.K_LEFT:
                cx_c = -5
            if event.key == pygame.K_RIGHT:
                cx_c = 5
            if event.key == pygame.K_UP:
                cy_c = -5
            if event.key == pygame.K_DOWN:
                cy_c = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                cx_c = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                cy_c = 0

    # cycle fun
    cx += cx_c
    cy += cy_c
    c_fun(cx, cy)
    if cx <= 0:
        cx = 0
    elif cx >= 1222:
        cx = 1222
        for i in range(no_of_obstacales):
            ox[i] = 30000
        w_fun()






    elif cy <= 0:
        cy = 0
    elif cy >= 602:
        cy = 602

    # obstacales fun

    for i in range(no_of_obstacales):
        ox[i] += ox_c[i]
        o_fun(ox[i], oy[i])
        if ox[i] <= 0:
            ox[i] = random.randint(128, 1286)
            oy[i] = random.randint(20, 666)

        # collusion fun
        collusion = collusion_fun(ox[i], oy[i], cx, cy)
        if collusion:
            cx = 0
            cy = 365
            # collusion sound
            # c_sound=mixer.sound('collusion sound.wav')
            # c_sound.play()

    # time limit fun
    elapsed_time = time.time() - start_time
    final_time = int(time_limit_value - elapsed_time)
    if elapsed_time > time_limit_value:
        final_time = 0
        g_fun()
        for i in range(no_of_obstacales):
            ox[i] = 30000
    t_fun()

