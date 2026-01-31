repeti = 's'

print('=' * 50)
print("Conversor de moedas")
rs = float(input("Quantos reais voçe tem na carteira? R$"))
print('=' * 50)
while repeti in ['s', 'sim', 'volta', 'voltar']:
    moeda = input('Qual tipo de moeda voçe deseja fazer a conversão? \n   [1=Dolar] [2=Euro] [3=Iene] [4=Yuan]  ')
    match moeda:
        case '1':
            res = rs * 0.19
            print(f"Com R${rs:.1f} voçe consegue comprar US${res:.2f}")
        case '2':
            res = rs * 0.16
            print(f'Com RS${rs} voçe consegue comprar €{res:.2f}')
        case '3':
            res = rs * 29.44
            print(f'Com R${rs:.1f} voçe consegue comprar Ienes ¥{res:.2f}')
        case '4':
            res = rs * 1.32
            print(f'Com R${rs:.1f} voçe consegue comprar Yuan ¥{res:.2f}')
        case _:
            print('Opção inválida!')
            
    repeti = input('Deseja fazer outra conversão? [S/N]').strip().lower()
print("Programa encerrado.")
