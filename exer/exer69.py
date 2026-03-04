extenso = ('Zero','Um','Dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
num = int(input('Digite um número entre 0 e 20: '))
while num <=0 or num >=20:
    num = int(input('Digite novamente, entre 0 e 20: '))
for pos, n in enumerate((extenso)):
    print(f'Voce digitou {extenso[num]}')
    break