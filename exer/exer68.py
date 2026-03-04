from time import sleep
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim','Batata Frita')
for comida in lanche:
    if comida == 'Suco':
        print(f'Eu vou tomar {comida}')
    else:
        print(f'Eu vou comer {comida}')
    sleep(1)