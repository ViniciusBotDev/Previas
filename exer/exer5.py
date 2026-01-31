metro = float(input('Digite seu metro: '))

dm = metro * 10
cm = metro * 100
mm = metro * 1000
dam = metro / 10
hm = metro / 100
km = metro / 1000

print(f'A medida de {metro:.0f} metros é igual a {dm:.0f} decímetros')
print(f'a medida de {metro:.0f} metros é igual a {cm:.0f} centrímetros')
print(f'A medida de {metro:.0f} metros é igual a {mm:.0f} milimetros')
print(f'A medida de {metro:.0f} metros é igual a {dam:.3f} decametros')
print(f'A medida de {metro:.0f} metros é igual a {hm:.3f} hectômetros')
print(f'A medida de {metro:.0f} metros é igual a {km:.3f} quilômetros')
