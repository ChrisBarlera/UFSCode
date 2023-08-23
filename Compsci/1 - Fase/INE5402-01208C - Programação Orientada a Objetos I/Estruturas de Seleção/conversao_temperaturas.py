def to_kelvin(origem, temperatura):
    if origem != 'k':
        if origem == 'c':
            temperatura = temperatura + 273.15
        elif origem == 'f':
            temperatura = (temperatura - 32) * 5/9 + 273.15
        elif origem == 'r':
            temperatura = temperatura * 5/9
    return temperatura


def converte_temperatura(origem, destino, temperatura):
    convertida = to_kelvin(origem, temperatura)

    if destino == 'c':
        convertida = convertida - 273.15
    elif destino == 'f':
        convertida = (convertida - 273.15) * 9/5 + 32
    elif destino == 'r':
        convertida = convertida * 1.8

    return convertida

origem = str.lower(input('Origem: '))
temperatura = float(input('Temperatura: '))
destino = str.lower(input('Destino: '))

temperatura = converte_temperatura(origem, destino, temperatura)

print(f'Temperatura convertida: {temperatura}')