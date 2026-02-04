import os
opçao = 'n'
catalogo = 'Qual produto deseja escolher? digite o Numero que deseja: \n [1]Laranja [2]Maça [3]Banana \n'
escolha_pagamento = int
valor = float
valorPix = float
valorCartão = float
quantidade = int
maça = 2.5
banana = 5
laranja = 8

print('Super Mercado')
print('Área de frutas')

while opçao in ['n', 'não']:
    produto = input(catalogo)
    match produto:
        case '1':
            quantidade = int(input('Cada Laranja custa R$8 \n mas pagando no pix tem %15 de desconto e no cartão %3 de aumento \n Quantas laranjas voçe quer? '))
            escolha_pagamento = input(f'Qual deseja Proseguir para ver os valores? [1] Dinheiro [2] Pix [3] Cartão voçe irá comprar {quantidade} unidades \n')
            if escolha_pagamento == '1':
                valor = laranja * quantidade
                pagar = input(f'Deseja pagar R${valor:.2f} por {quantidade} quantidades de laranjas? [S/N] \n').strip().lower()
                if pagar in ['s', 'sim']:
                    print(f'Obrigado pela compra maçãs pelo valor de R${valor:.2f}')
                    break
                else:
                    print('Ok voltando...')
                    opçao = 'n'

            elif escolha_pagamento == '2':
                valorPix = laranja * quantidade
                valorPix = laranja - (valorPix * 15 / 100)
                print(f'este será o valor com desconto R${valorPix:.2f}')
                pagar = input(f'Deseja pagar R${valorPix:.2f} por {quantidade} quantidades de maçã? [S/N] \n').strip().lower()
                if pagar in ['s', 'sim']:
                    print(f'Obrigado pela compra da Laranja de R${valorPix:.2f}')
                    break
                else:
                    print('Ok voltando...')
                    opçao = 'n'

            elif escolha_pagamento == '3':
                valorCartão = laranja * quantidade
                valorCartão = laranja + (valorCartão * 5 / 100)
                print(f'Este será o valor com aumento R${valorCartão:.2f}')
                pagar = (f'Deseja pagar R${valorCartão:.2f} por {quantidade} quantidades de laranjas? [S/N] \n').strip().lower()
                if pagar in ['s', 'sim']:
                    print(f'Obrigado pela compra da Laranja de R${valorCartão:.2f}')
                    break
                else:
                    print('Ok Voltando...')
                    opçao = 'n'

        case '2' :
            quantidade = int(input('Cada Maça custa R$2.50 \n mas pagando no pix tem %15 de desconto e no cartão %3 de aumento \n Quantas maçãs voçe quer? '))
            escolha_pagamento = input(f'Qual deseja Proseguir para ver os valores? [1] Dinheiro [2] Pix [3] Cartão voçe irá comprar {quantidade} unidades \n')
            if escolha_pagamento == '1':
                valor = maça * quantidade
                pagar = input(f'Deseja pagar R${valor:.2f} por {quantidade} quantidades de maçã? [S/N] \n').strip().lower()
                if pagar in ['s', 'sim']:
                    print(f'Obrigado pela compra maçãs pelo valor de R${valor:.2f}')
                    break
                else:
                    print('Ok voltando...')
                    opçao = 'n'

            if escolha_pagamento == '2':
                valorPix = maça * quantidade
                valorPix = maça - (valorPix * 15 / 100)
                pagar = input(f'Deseja pagar R${valorPix:.2f} por {quantidade} quantidades de maçã? [S/N] \n').strip().lower()
                if pagar in ['s', 'sim']:
                    print(f'Obrigado pela compra de maçãs pelo valor de R${valorPix:.2f}')
                    break
                else: 
                    print('Ok voltando...')
                    opçao = 'n'

            if escolha_pagamento == '3':
                valorCartão = maça * quantidade
                valorCartão = maça + (valorCartão * 15 / 100)
                pagar = (f'Deseja pagar R${valorCartão:.2f} por {quantidade} quantidades de maçã? [S/N] \n').strip().lower()
                if pagar in ['s', 'sim']:
                    print(f'Obrigado pela compra maçã pelo valor de R${valorCartão:.2f}')
                    break
                else:
                    print('Ok voltando...')
                    opçao = 'n'
            
        case '3':
            quantidade = int(input('Cada banana custa R$5 \n mas pagando no pix tem %15 de desconto e no cartão %3 de aumento \n Quantas maçãs voçe quer? '))
            escolha_pagamento = input(f'Qual deseja Proseguir para ver os valores? [1] Dinheiro [2] Pix [3] Cartão voçe irá comprar {quantidade} unidades \n')
            if escolha_pagamento == '1':
                valor = banana * quantidade
                pagar = input(f'Deseja pagar R${valor:.2f} por {quantidade} quantidade de bananas? [S/N] \n').strip().lower()
                if pagar in ['s', 'sim']:
                    print(f'Obrigado pela compra de bananas no valor de R${valor:.2f}')
                    break
                else:
                    print('Ok voltando...')
                    opçao = 'n'

            if escolha_pagamento == '2':
                valorPix = banana * quantidade
                valorPix = banana - (valorPix * 15 / 100)
                pagar = input(f'Deseja pagar R${valorPix:.2f} por {quantidade} quantidades de banana? [S/N] \n').strip().lower()
                if pagar in ['s', 'sim']:
                    print(f'Obrigado pela compra de bananas no valor de R${valorPix:.2f}')
                    break
                else: 
                    print('Ok voltando...')
                    opçao = 'n'

            if escolha_pagamento == '3':
                valorCartão = banana * quantidade
                valorCartão = banana + (valorCartão * 15 / 100)
                pagar = (f'Deseja pagar R${valorCartão:.2f} por {quantidade} quantidades de banana? [S/N] \n').strip().lower()
                if pagar in ['s', 'sim']:
                    print(f'Obrigado pela compra de bananas no valor de R${valorCartão:.2f}')
                    break
                else:
                    print('Ok voltando...')
                    opçao = 'n'
                    