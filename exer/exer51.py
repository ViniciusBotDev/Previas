from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    pessoas = int(input(f'Digite que ano essa pessoa nasceu {c}:  '))
    idade = atual - pessoas
    if pessoas >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade')
