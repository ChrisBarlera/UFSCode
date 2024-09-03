from banco import Banco

bc = Banco("Banco do Brejo", 999)

try:
    while True:
        entrada = input().split()
        match entrada[0]:
            case 'abre_conta':
                bc.abre_conta(entrada[2], entrada[1])
            case 'deposito':
                bc.deposito(entrada[1], entrada[2])
            case 'transferencia':
                bc.transferencia(entrada[1], entrada[2], entrada[3])
            case 'saque':
                bc.saque(entrada[1], entrada[2])
except EOFError:
    pass