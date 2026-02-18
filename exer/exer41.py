altura = float(input('Digite sua altura:  '))
peso = float(input('Digite sua massa(KG):  '))
imc = peso / (altura ** 2)
print(f'O IMC desta pessoa é de {imc:.1f}')
if imc < 18.5:
    print("Muito abaixo do Peso")
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <=  imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade, cuidado!')
else:
    print('obesidade morbida, cuidado!')
