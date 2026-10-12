import pygame

class Controle:

    def __init__(self, indice):

        self.indice = indice

        if self.indice in range(pygame.joystick.get_count()):
            #validar se o indice do controle é valido
            self.controle = pygame.joystick.Joystick(self.indice)
            self.controle.init()
        else:
            raise ValueError("Indice de controle Inválido")

    def obter_direcao(self):
        # retorna uma tupla com os valores dos eixos do controle
        valor_x = self.controle.get_axis(0)
        valor_y = self.controle.get_axis(1)

        return (valor_x, valor_y)