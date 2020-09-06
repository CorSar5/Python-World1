print('Pedir-lhe-ei para me dar três comprimentos, e se estes conseguem formar um triângulo:')
print('-_-'*20)
a = float(input('Primeira medida: '))
b = float(input('Segunda medida: '))
c = float(input('Terceira medida: '))

print('-_-'*20)
if (b-c)<a<b+c and (a-c)<b<a+c and (a-b)<c<a+b  and a == b and b == c :
    print(f'Sim com as medidas: {a}, {b} e {c} é possível formar um triângulo')
    print('Este triângulo será equilátro!')
if (b-c)<a<b+c and (a-c)<b<a+c and (a-b)<c<a+b and a== b and b!=c or b==c and c!=a or  a==c and c!=b:
    print(f'Sim com as medidas: {a}, {b} e {c} é possível formar um triângulo')
    print('Este triângulo será isósceles!')
if (b-c)<a<b+c and (a-c)<b<a+c and (a-b)<c<a+b and a!=b!=c:
    print(f'Sim com as medidas: {a}, {b} e {c} é possível formar um triângulo')
    print('Este triângulo será escaleno!')
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print(20*'.')
else:
    print(f'Não, com as medidas {a}, {b} e {c} não é possível formar um triângulo')
print('-_-'*20)
