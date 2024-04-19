def get_x_pos(matriz):
    x_pos = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i,j] == 'X':
                x_pos.append(i)
                x_pos.append(i,j)
                return x_pos

def umTunel():
    n_linha, n_col = [int(x) for x in input().split()]
    matriz = []
    movimentos = ''
    for _ in range(n_linha):
        matriz.append(input().split())
    
    # achar o x
    x_pos = get_x_pos(matriz)
    temp_pos = x_pos.copy()

    # ver pra qual lado ele vai
    if x_pos[0] + 1 < n_linha:
        if x_pos[0] + 1 == '0':
            x_pos[0] += 1
            movimentos += 'F '
    
    if x_pos[0] - 1 >= 0:
        if x_pos[0] + 1 == '0':
            x_pos[0] += 1
    # ir pra la
    # onde tava antes vira 1
    # acaba quando estiver cercado de 1 e/ou num canto

umTunel()