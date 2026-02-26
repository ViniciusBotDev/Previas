sexo = str(input('Qual seu sexo? [M/F]:  ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados invalidos informe qual seu sexo? [M/F]:  ')).strip().upper()[0]
if sexo == 'F':
    print('Sexo registrado: Feminino')
else:
    print('Sexo registrado: Masculino')
    