import turtle

def poligono_regular(tartaruga, n_lados, tamanho_lado):
    soma = (n_lados - 2) * 180
    angulo_externo = 180-(soma/n_lados)
    for _ in range(n_lados):
        tartaruga.forward(tamanho_lado)
        tartaruga.left(angulo_externo)

tortuga = turtle.Turtle()
n_lados = 10
tamanho_lado = 50

poligono_regular(tortuga, n_lados, tamanho_lado)
turtle.done()