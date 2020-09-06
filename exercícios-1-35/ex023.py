x = int(input('Digite um número de 0 a 9999:'))
u = x //1 % 10
d = x //10 % 10
c = x //100 % 10
m = x // 1000 % 10
print(f'Analisando o número {x}...')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')