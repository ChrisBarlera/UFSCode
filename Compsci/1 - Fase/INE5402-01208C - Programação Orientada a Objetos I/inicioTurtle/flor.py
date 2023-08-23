import turtle

def caule(tartaruga):
    tartaruga.width(raio/20)
    tartaruga.left(90)
    tartaruga.forward(raio)
    tartaruga.right(90)
    tartaruga.width(1)
    petala(tartaruga, raio, arco)
    tartaruga.left(90)
    tartaruga.width(raio/20)
    tartaruga.forward(raio)
    tartaruga.width(1)

def petala(tartaruga, raio, arco):
    tartaruga.fillcolor('red')
    tartaruga.begin_fill()
    for _ in range(2):
        tartaruga.circle(raio, arco)
        tartaruga.left(180-arco)
    tartaruga.end_fill()
def flor(tartaruga):    
    for _ in range(numero_petalas):
        petala(tartaruga, raio, arco)
        tartaruga.left(360/numero_petalas)


tortuga = turtle.Turtle()
# tortuga.speed(0)

raio = 100

# numero_petalas = int(input('Número de pétalas: '))
# arco = int(input('Tamanho do arco: '))

numero_petalas = 7
arco = 60

soma_angulos_internos = (numero_petalas-2) * 180
angulo_interno = soma_angulos_internos/numero_petalas

caule(tortuga)
flor(tortuga)

turtle.done()