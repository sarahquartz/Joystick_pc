import pyautogui

class Mouse:

    def __init__(self, velocidade_mouse):
        self.largura_tela, self.altura_tela = pyautogui.size()
        self.velocidade_mouse = velocidade_mouse


    def mover(self, direcao, delta_t):
        #Movimenta o mouse com base em uma velocidade constante e um intervalo de tempo
        #Limita o movimento ao tamanho da tela

        dx, dy = direcao
        dx = dx ** 3
        dy = dy ** 3
        dx = dx * self.velocidade_mouse * delta_t
        dy = dy * self.velocidade_mouse * delta_t
        

        x_atual, y_atual = pyautogui.position()
        x_desejado, y_desejado = x_atual + dx, y_atual + dy

        x_permitido = max(0 , min(x_desejado, self.largura_tela -1))
        y_permitido = max(0 , min(y_desejado, self.altura_tela -1))

        dx_final = x_permitido - x_atual
        dy_final = y_permitido - y_atual

        pyautogui.moveRel(dx_final, dy_final)
        return pyautogui.position()

