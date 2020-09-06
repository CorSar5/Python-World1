frase = str(input('Esceva uma frase sobre o Verão:')).strip().upper()
print('A letra "A" no seu texto aparece {} vezes'.format(frase.count('A')))
print('Aparece pela 1ª vez na posição {}'.format(frase.find('A')+1))
print('E aparece pela última na {} posição'.format(frase.rfind('A')+1))

frase = str(input('Digite uma frase:')).strip().lower()
print('Existem {} "a" na sua frase'.format(frase.count('a')) )
print('O primeiro "a" aparece nas posição {}'.format(frase.find('a')+1))
print('A última vez que um "a" aparece é na posição {}'.format(frase.rfind('a')+1))
