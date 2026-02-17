print('Contador de Médias')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
    
nota = (n1 + n2 + n3) / 3
print(f'''Tirando {n1:.1f} e {n2:.1f} e {n3:.1f}
Sua nota média final é {nota:.1f}''')
if nota >= 9.0:
    print('Parabéns sua nota está otima!')
elif nota >= 7.0:
    print('Está bom mas pode ser melhor!')
elif nota >= 6.0:
    print('Cuidado da Próxima vez, melhore!')
elif nota >= 5:
    print('Voçe está de recuperação!')
else:
    print('Voçe não consegiu a média, melhore da próxima')
