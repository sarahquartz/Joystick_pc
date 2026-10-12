import os
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"
import pygame
import time
import pyautogui
from controle import Controle
from mouse import Mouse

pygame.init()
pygame.event.set_grab(False)
janela = pygame.display.set_mode((400,300))
pygame.joystick.init()
print("Quantidade de controles:", pygame.joystick.get_count())

controle_1 = Controle(0)
mouse = Mouse(300)

executando = True
temopo_anterior = time.time()
while executando:
    pygame.event.pump()
    for event in pygame.event.get():
        #Sair
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print("ESC detectado!")
            executando = False

        #Detectar botão 0 do controle precionado
        if controle_1.detectar_botao(event, 0):
            print(f"Botão 0 pressionado")
            mouse.clicar()

    if not executando:
        break

    #movimentação do mouse pelo controle
    direcao = controle_1.obter_direcao()
    tempo_atual = time.time()
    delta_t = min((tempo_atual - temopo_anterior), 0.1)
    mouse.mover(direcao, delta_t)
    temopo_anterior = tempo_atual
    

    

