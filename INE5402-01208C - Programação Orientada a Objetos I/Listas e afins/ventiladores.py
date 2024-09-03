# # def ileso(linha, pos):
# #     pass
# linhas, colunas, pos = [int(x) for x in input().split()]
# while colunas !=0 and linhas != 0 and pos != 0:
#     pos -= 1


linhas, colunas, pos = [int(x) for x in input().split()]
pos -= 1

ileso = True
l_pos = 0
novo_i = pos
for i in range(linhas):
    linha = [int(x) for x in input().split()]
    
    # if i != 0:
    #     if linha[novo_i] != 0:
    #         ileso = False
    #         l_pos = i+1
    #         novo_i += 1
    #         break
    direita = max(linha[novo_i::]) # n fununfa (pode ter 3 ventilador)
    esquerda = max(linha[0:novo_i])
    
    novo_i = pos + (esquerda - direita) #fununfa

print(f'OUT {novo_i}' if ileso else f'BOOM {l_pos}')