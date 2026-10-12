import pygame
import time
import pyautogui
from controle import Controle
from mouse import Mouse

pygame.init()
janela = pygame.display.set_mode((400,300))
pygame.joystick.init()

controle_1 = Controle(0)
mouse = Mouse(300)

executando = True
temopo_anterior = time.time()
while executando:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print("ESC detectado!")
            executando = False

    if not executando:
        break

    #movimentação do mouse pelo controle
    direcao = controle_1.obter_direcao()
    tempo_atual = time.time()
    delta_t = min((tempo_atual - temopo_anterior), 0.1)
    print(delta_t)
    mouse.mover(direcao, delta_t)
    temopo_anterior = tempo_atual
    

    

