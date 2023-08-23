import turtle

t = turtle.Turtle()
t.speed(0)


TAMANHO = 50
AMPLITUDE = 1000

for i in range(AMPLITUDE):
    t.forward(TAMANHO+1.5*i)
    t.left(89)
turtle.done()