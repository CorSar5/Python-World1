from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que deseja:'))
seno = sin(radians(angulo))
print('O ângulo de {} tem o Seno de {}'.format(angulo,seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o Cosseno de {}'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print('O ângulo {} term a Tangente de {}'.format(angulo, tangente))