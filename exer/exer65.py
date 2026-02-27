total_pessoas18 = total_homens = total_mulheres20 = 0
while True:
    print('-'*30)
    print('     Cadastre uma pessoa')
    print('-'*30)
    idade = int(input('idade:   '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        print('Digite apenas M ou F!')
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    if sexo == 'M':
        total_homens += 1
    if idade >= 18 and sexo in 'MF':
        total_pessoas18 += 1
    if sexo == 'F' and idade < 20:
        total_mulheres20 += 1
    escolha = str(input('Deseja continuar [S/N]:  ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Digite apenas [S/N]: ')
        escolha = str(input('Deseja continuar [S/N]:  ')).strip().upper()[0]
    if escolha == 'N':
        break
print('='*5,' FIM DO PROGRAMA ','='*5)
print(f'''Total de pessoas com mais de 18 anos: {total_pessoas18}
Ao todo temos {total_homens} homens cadastrados
E temos {total_mulheres20} com menos de 20 anos''')
