conceitos_aluno = [input().upper() for _ in range(4)]
tabela_conceitos = {'A':4, 'B':3, 'C':2, 'E':0}
ia = 0
for conceito in conceitos_aluno:
    ia += tabela_conceitos[conceito] / len(conceitos_aluno)

aprovado = 'E' not in conceitos_aluno and ia >= 3
