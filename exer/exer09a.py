from math import hypot

cat_ops = float(input('Digite um cateto:   '))
cat_adj = float(input('Digite outro cateto:   '))
hi = hypot(cat_ops, cat_adj)

print(f'A hipotenusa de {cat_ops} e {cat_adj} é {hi:.2f}')