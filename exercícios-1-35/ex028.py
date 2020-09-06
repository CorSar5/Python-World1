from random import randint
computador = randint(0,5)
print('-=-'*10)
print('Pensei num número entre 0 e 5.')
r = int(input( 'Tente adivinhar:'))
print('-=-'*10)
print('O número que pensei foi: {}'.format(computador))
if computador == r:
    print('Parabéns você acertou')
else :
    print('Não conseguiu adivinhar.')
print('-=-'*10)
