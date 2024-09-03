import turtle as t

tartaruga = t.Turtle()
x = 170

def retangulo(altura, base, cor, turtle):
    turtle.fillcolor(cor)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(base)
        turtle.left(90)
        turtle.forward(altura)
        turtle.left(90)
    
    turtle.end_fill()

# Base
retangulo(
    altura=x,
    base=2*x,
    cor='#FF5F5F',
    turtle=tartaruga
)

# Janela 1
## Chegando no lugar
tartaruga.up()
tartaruga.forward(x/4)
tartaruga.left(90)
tartaruga.forward(x/3)
tartaruga.right(90)
tartaruga.down()
## Desenhando janela
retangulo(
    altura=x/3,
    base=x/3,
    cor='#B0F7FF',
    turtle=tartaruga
)

# Porta
## Chegando no lugar
tartaruga.up()
tartaruga.right(90)
tartaruga.forward(x/3)
tartaruga.left(90)
tartaruga.forward(7*x/12)
tartaruga.down()
## Desenhando
retangulo(
    altura=2*x/3,
    base=x/3,
    cor='#570202',
    turtle=tartaruga
)

# Janela 2
## Chegando na janela
tartaruga.up()
tartaruga.forward(7*x/12)
tartaruga.left(90)
tartaruga.forward(x/3)
tartaruga.right(90)
tartaruga.down()
## Desenhando janela
retangulo(
    altura=x/3,
    base=x/3,
    cor='#B0F7FF',
    turtle=tartaruga
)

# Beiral
## Chegando no beiral
tartaruga.up()
tartaruga.backward(2*x-7*x/12)
tartaruga.left(90)
tartaruga.forward(2*x/3)
tartaruga.left(90)
tartaruga.forward(x/6)
tartaruga.left(180)
tartaruga.down()
## Desenhando
retangulo(
    altura=x/6,
    base=2*x+2*x/6,
    cor='#582F01',
    turtle=tartaruga
)

# Teto
## Chegando no teto
tartaruga.up()
tartaruga.left(90)
tartaruga.forward(x/6)
tartaruga.right(90)
tartaruga.forward(x/6)
tartaruga.down()
## Desenhando
tartaruga.fillcolor('#A85900')
tartaruga.begin_fill()
tartaruga.left(45)
tartaruga.forward(x*2**(1/2))
tartaruga.right(90)
tartaruga.forward(x*2**(1/2))
tartaruga.end_fill()


t.done()