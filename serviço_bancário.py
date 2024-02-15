menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Quanto gostaria de depositar?: R$'))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print('Operação falhou! O valor informado é inválido.')
    elif opcao == 's':
        valor = float(input('Quanto deseja sacar: R$'))

        saldo_insuficiente = valor > saldo

        limite_insuficiente = valor > limite

        saques_esgotados = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print('Operação cancelada! Saldo insuficiente.')

        elif limite_insuficiente:
            print('Operação cancelada! Saque acima do limite.')
        elif saques_esgotados:
            print('Operação cancelada! Sem saques disponíveis.')
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print('Operação cancelada! Valor inválido.')
    elif opcao == 'e':
        print('============EXTRATO============')
        print('Não foram realizads movimentaçãoes.' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print('========================')

    elif opcao == 'q':
        print('Você escolheu interromper seu atendimento, até logo.')
        break

    else:
        print('Operação inválida! Selecione uma opção válida.')


        
    