km = float(input('Digite a distância da sua viagem: '))
if km >200:
    mm = km*0.45
    print('Parece que a sua viagem ultrapassará os 200km terá então um desconto')
    print('A sua viagem costará {}$,.'.format(mm))
else :
    mp = km*0.50
    print('A sua viagem irá custar {}$.'.format(mp))
print('Efetue o pagamento por cartão ou dinheiro, Obrigado!')