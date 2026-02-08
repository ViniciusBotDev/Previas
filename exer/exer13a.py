frase = str(input('Digite uma frase:  ')).lower().strip()

print(f'A quantidade de A que tem nessa frase é: {(frase.count('a'))}')
print(f'A primeira posição que o A aparece é: {(frase.find('a'))}')
print(f'A ultima posição que o A aparece é: {(frase.rfind('a'))}')