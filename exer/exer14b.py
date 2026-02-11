velocidade_atual = float(input('Que velocidade o carro está?  '))
if velocidade_atual > 80:
    excesso = velocidade_atual - 80
    valor_multa = excesso * 7
    print(f'Voçe foi multado no valor de {valor_multa:.2f} por ultrapassar 80kmh')
else:
    print('Boa viagem')