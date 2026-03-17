pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['media'] = float(input(f'Media de {pessoa["nome"]}: '))
if pessoa['media'] >= 6:
    pessoa['situação'] = 'Aprovado'
elif pessoa['media'] >= 4:
    pessoa['situação'] = 'Recuperação'
else:
    pessoa['situação'] = 'Reprovado'
print('='*30)
for k, v in pessoa.items():
    print(f' - {k} é igual a {v}')

