import math

angulo = float(input('Digite o ângulo que voçe deseja: '))
radianos = math.radians(angulo)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')