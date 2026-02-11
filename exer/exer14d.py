distancia = int(input('Digite a distancia que voçe percorreu:  '))
if distancia > 200:
    km_rodado = (distancia - 200) * 0.45
    print(f'Voçe percorreu {distancia} com valor total de R${km_rodado}')
else:
    km_rodado = distancia * 0.50
    print(f'Voçe percorreu a distancia de {distancia} com valor total de R${km_rodado} ')