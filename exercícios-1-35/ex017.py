'''import math
ca = float(input('Escreva o comprimento do cateto adjacente:'))
co = float(input('Escreva o comprimento do cateto oposto:'))
hp = math.sqrt(co**2 + ca**2)
print('Um triângulo com a medida {} no cateto adjacente e {} no cateto oposto, tem de comprimento da hipotenusa {}'.format(ca, co, hp))'''

import math
ca = float(input('Escreva o comprimento do cateto adjacente:'))
co = float(input('Escreva o comprimento do cateto oposto:'))
hi = math.hypot(co,ca)
print(f'A hipotenusa vai medir {hi}')