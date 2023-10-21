while True:
    try:
        frase = input().lower()
        palavras = frase.split('-')

        cobol = 'cobol'
        resultado = 'GRACE HOPPER'
        for i in range(len(palavras)):
            if palavras[i][0] == cobol[i] or palavras[i][-1] == cobol[i]:
                pass
            else:
                resultado = 'BUG'

        print(resultado)
    except EOFError:
        break