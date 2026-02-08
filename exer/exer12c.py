cidade = str(input('Digite o nome da sua cidade:  ')).lower()

print(f'Sua cidade contém Santo: {(cidade.startswith('santo'))}')

nome = str(input('Digite seu nome:  ')).lower()
print(f'Seu nome contém Silva: {('silva' in nome)}')