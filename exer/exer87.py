from datetime import date
carteira = {}
carteira['nome'] = str(input('Digite seu nome: '))
carteira['nascimento'] = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - carteira['nascimento']
carteira['idade'] = idade
carteira['ctps'] = int(input('Digite o número da carteira de trabalho (0 se não tiver): '))
if carteira['ctps'] != 0:
    carteira['contratação'] = int(input('Digite o ano de contratação: '))
    carteira['salário'] = float(input('Digite o salário: R$'))
    carteira['aposentadoria'] = carteira['idade'] + ((carteira['contratação'] + 35) - date.today().year)
for k, v in carteira.items():
    print(f'{k} tem o valor {v}')

