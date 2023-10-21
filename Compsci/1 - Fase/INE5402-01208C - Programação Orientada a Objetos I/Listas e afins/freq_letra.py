frase = input().replace(' ','')
letras = list(set(frase))

mais_freq = letras[0]
cont_freq = frase.count(letras[0])
for letra in letras:
    freq_letra = frase.count(letra)
    if freq_letra > cont_freq:
        mais_freq = letra
        cont_freq = freq_letra

print(mais_freq)