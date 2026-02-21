saldo = 1000.0
historico = []
contagem = 0

while True:
    print('----- Menu -----')
    print('1. ver Saldo\n2. Depositar\n3. Sacar\n4. Ver histórico\n5. Sair')
    opção = int(input('Digite uma opção:  '))

    if opção == 1:
        print(f'Seu saldo atual é: R${saldo:.2f}')
    elif opção == 2:
        valor = float(input('Quanto dinheiro voçe deseja depositar:  R$'))
        saldo += valor
        historico.append(f'Depósito: + R${valor:.2f}')
        print('Depósito realizado!')
        contagem += 1
    elif opção == 3:
        print(f'Este é seu saldo atual R${saldo} quanto voçe deseja sacar? Minímo R$10')
        saque = float(input('Sacar R$'))
        if saque <= saldo and saque >= 10:
            saldo -= saque
            historico.append(f'Saque: - R${saque:.2f}')
            print(f'Voçe sacou R${saque} e agora seu saldo atual é R${saldo}')
            contagem += 1
        else:
            print('Não é possivel sacar esté valor')
    elif opção == 4:
        print('--- Extrato Detalhado ---')
        if len(historico) == 0:
            print('Nenhuma transação realizada ainda.')
        else:
            for operação in historico:
                print(f'Movimentação: {operação}')
            print(f'Transições realizadas: {contagem}')
    elif opção == 5:
        print('SAINDO...')
        break
    else:
        print('Opção inválida..')
