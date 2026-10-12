# Controle de Mouse por Joystick

Projeto em Python para controlar o cursor do mouse utilizando um controle físico conectado ao computador.

## Funcionalidades

- Leitura da direção dos analógicos do controle.
- Movimentação do cursor do mouse com base na direção do analógico.
- Ajuste da velocidade de movimento conforme a inclinação do analógico.
- Limitação do movimento às bordas da tela.

## Tecnologias utilizadas

- Python
- Pygame
- PyAutoGUI

## Requisitos

- Python 3
- Um controle compatível com Pygame
- Sistema Linux com acesso ao controle e permissão para controlar o mouse

## Instalação

Clone o repositório e entre na pasta do projeto. Em seguida, crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## Execução

Com o ambiente virtual ativado, execute o arquivo principal do projeto:

```bash
python main.py
```

Substitua `main.py` pelo nome correto do seu arquivo principal, se for diferente.

## Encerramento

Pressione `Esc` para encerrar o programa, caso essa funcionalidade esteja habilitada.

## Status do projeto

Em desenvolvimento. Novas funcionalidades e melhorias de controle poderão ser adicionadas futuramente.
