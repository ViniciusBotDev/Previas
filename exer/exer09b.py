from math import radians, cos, sin, tan

angulo = float(input('Digite o ângulo que voçe deseja: '))
radianos = radians(angulo)

seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)

print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo} tem o COSSENO  de {cosseno:.2f}')
print(F'o Ângulo de {angulo} tem o TANGENTE de {tangente}')