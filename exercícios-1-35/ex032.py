ano = int(input('Digite um ano e eu direi se é um ano bissexto ou não:'))
anob = ano % 4
if anob == 0 and anob % 100!=0 or ano % 400 == 0:
    print('Esse ano ({}) é bissexto, tendo em fevereiro 29 dias, e 366 dias no total'.format(ano))
else :
    print('Esse ano({}) não será bissexto, terá apenas 365 dias.'.format(ano))
print('Pensava que me ia enganar? Eu não falho!')