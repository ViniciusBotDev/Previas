from datetime import date

Genêro = input('Voçe é homem ou mulher?  ').strip().lower()
if Genêro == 'mulher':
    print('Voçe não precisa se alistar.')
else:
    ano_atual = date.today().year
    nascimento = int(input('Que ano voçe nasceu?:  '))
    sua_idade = ano_atual - nascimento
    print(f'Quem nasceu em {nascimento} tem {sua_idade} anos em {ano_atual}')
    if sua_idade == 18:
        print('Voçe deve se alistar imediatamente')
    elif sua_idade < 18:
        saldo = 18 - sua_idade
        print(f'Ainda faltam {saldo} anos para se alistar')
        ano = ano_atual + saldo
        print(f'Seu alistamento será em {ano}')
    elif sua_idade > 18:
        saldo = sua_idade - 18
        print(f'Voçe ja deveria ter se alistado a {saldo} anos')
        ano = ano_atual - saldo
        print(f'Seu alistamento foi em {ano}')
