from datetime import date

print('Confederação Nacional de Natação')
nascimento = int(input('Insira o ano em que voçe nasceu:  '))
ano_atual = date.today().year
idade = ano_atual - nascimento
if idade <= 9:
    print('Voçe está na categoria: Mirim!')
elif idade <= 14:
    print('Voçe está na categoria: Infantil!')
elif idade <= 19:
    print('Voçe está na categoria: Junior!')
elif idade <= 25:
    print('Voçe está na categoria: Seniôr!')
else:
    print('Voçe está na categoria: Master!')