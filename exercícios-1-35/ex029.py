print('_-=-_'*20)
v = int(input('Digite a velocidade que o seu carro está a mover-se:'))
print('_-=-_'*20)
if v>80 :
    m = (v-80)*1.10
    print('A sua velocidade está demasiado acima. O limite são 80km/h !Poderá apanhar uma multa de {} €!'.format(m))
else :
    print('Parabéns!!Continue com a velocidade moderada!!')
print('Lembre-se sempre, segurança em 1º lugar!')
print('_-=-_'*20)