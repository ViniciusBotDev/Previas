valor_casa = float(input('Qual o valor da casa que deseja comprar?  R$'))
salario = float(input('Digite seu salário R$'))
tempo = int(input('Em quantos anos deseja pagar a casa: '))
prestação = valor_casa / (tempo * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${valor_casa} em {tempo} Anos')
print(f'O valor da prestação será de {prestação:.2f}')
if prestação >= minimo:
    print('Epréstimo Negado.')
else:
    print('Empréstimo Concedido!')
