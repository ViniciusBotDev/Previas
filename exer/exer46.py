num = int(input('Qual tabuada deseja ver?  '))
vezes = int(input('Quantas vezes?  '))
for c in range(1, vezes+1,):
    soma = num * c
    print(f' {c} x {num} = {soma}')