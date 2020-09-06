s = float(input('Escreva o valor do seu salário:'))
if s> 900:
    m = s + s*0.1
    print(f'Com o aumento passará a receber de {s} para {m}')
else:
    m = s +s*0.15
    print(f'Com o aumento de 15% passará a receber de {s} a {m}')