Numero = int(input('Digite um Numero:  '))
print('''Escolha uma base para conversão:'
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')
opção = int(input('Sua opção:  '))
if opção == 1:
    print(f'{Numero} convertido para Binário é igual a {bin(Numero)[2:]}')
elif opção == 2:
    print(f'{Numero} convertido para Octal é igual a {oct(Numero)[2:]}')
elif opção == 3:
    print(f'{Numero} convertido para Hexadecimal é igual a {hex(Numero)[2:]}')
else:
    print('Opção Inválida.')